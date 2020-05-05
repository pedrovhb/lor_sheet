import io
import json

import requests
import tempfile
import zipfile
import pathlib
import os
from PIL import Image

# Avoid hardcoding paths and using cross-platform path joins
file_dir = pathlib.Path(__file__).parent.absolute()
src_dir = os.path.join(file_dir, "lor_sheet", "src")
public_dir = os.path.join(file_dir, "lor_sheet", "public")

card_image_output_dir = os.path.join(public_dir, "img", "cards")
processed_data_path = os.path.join(src_dir, "card_data", "processed_data.json")


def get_core_data():
    # The zipfile module requires named files and can't load straight
    # from binary data, so we create temporary files to extract downloaded
    # data.

    # Core set data includes region data
    with tempfile.NamedTemporaryFile("ba+") as fd_core:
        r = requests.get("https://dd.b.pvp.net/latest/core-en_us.zip")
        fd_core.write(r.content)
        fd_core.seek(0)

        with zipfile.ZipFile(fd_core.name) as zf:
            core_data = zf.read("en_us/data/globals-en_us.json").decode()
            core_data = json.loads(core_data)
            return core_data


def get_set_data(set_number):
    # Set data includes card info. This function returns card data and also
    # converts card images to .webp, storing them in the public data dir to
    # be served statically.
    with tempfile.NamedTemporaryFile("ba+") as fd_set:
        r = requests.get(
            f"https://dd.b.pvp.net/latest/set{set_number}-lite-en_us.zip"
        )
        fd_set.write(r.content)
        fd_set.seek(0)

        with zipfile.ZipFile(fd_set.name) as zf:

            print("Writing images...")
            for file in zf.filelist:
                filename = os.path.split(file.filename)[-1]
                base, ext = os.path.splitext(filename)
                if ext == ".png" and "-alt" not in filename:
                    memfile = io.BytesIO(zf.read(file.filename))
                    im = Image.open(memfile)
                    output_fpath = os.path.join(card_image_output_dir, base)

                    # Save webp image
                    im.save(output_fpath + ".webp", "WEBP")

                    # Save downsized jpg image
                    jpg = Image.new("RGB", im.size, (255, 255, 255))
                    jpg.paste(im, mask=im.split()[3])
                    jpg.thumbnail((900, 900), Image.ANTIALIAS)
                    jpg.save(output_fpath + ".jpg", "JPEG", quality=70)

            # Return json card data
            card_data = zf.read(f"en_us/data/set{set_number}-en_us.json")
            return json.loads(card_data.decode("utf-8"))


processed_data = {"regions": {}, "cards": []}

print("Getting core data...")
core_data = get_core_data()
for region in core_data["regions"]:
    processed_data["regions"][region["nameRef"]] = {
        "name": region["name"],
        "nameRef": region["nameRef"],
        "iconPath": region["iconAbsolutePath"].split("/")[-1],
    }

print("Getting set data...")
set_data = get_set_data(1)
set_data.extend(get_set_data(2))
for card in set_data:
    processed_data["cards"].append(
        {
            "name": card["name"],
            "regionRef": card["regionRef"],
            "cost": card["cost"],
            "code": card["cardCode"],
            "speed": card["spellSpeed"],
        }
    )


print("Writing processed data to file...")
with open(processed_data_path, "w", encoding="utf-8",) as fd:
    json.dump(processed_data, fd)
