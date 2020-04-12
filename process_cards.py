import io
import json
import os
import pathlib

import requests
from PIL import Image

file_dir = pathlib.Path(__file__).parent.absolute()
src_dir = os.path.join(file_dir, "lor_sheet", "src")
public_dir = os.path.join(file_dir, "lor_sheet", "public")

original_data_dir = os.path.join(src_dir, "card_data", "orig_data")
card_image_output_dir = os.path.join(public_dir, "img", "cards")

processed_data = {}

print("Loading game data...")
with open(os.path.join(original_data_dir, "globals-en_us.json"), encoding="utf-8") as fd:
    core_data = json.load(fd)
with open(os.path.join(original_data_dir, "set1-en_us.json"), encoding="utf-8") as fd:
    set_data = json.load(fd)

print("Processing region data...")
processed_data["regions"] = {}
for region in core_data["regions"]:
    processed_data["regions"][region["nameRef"]] = {
        "name": region["name"],
        "nameRef": region["nameRef"],
        "iconPath": region["iconAbsolutePath"].split("/")[-1]
    }

print("Processing card data...")
processed_data["cards"] = []
to_download = []
for card in set_data:
    to_download.append(card["assets"][0]["gameAbsolutePath"])
    processed_data["cards"].append({
        "name": card["name"],
        "regionRef": card["regionRef"],
        "cost": card["cost"],
        "code": card["cardCode"],
        "speed": card["spellSpeed"]
    })

print("Writing processed data to file...")
with open(os.path.join(src_dir, "card_data", "processed_data.json"), "w", encoding="utf-8") as fd:
    json.dump(processed_data, fd)

for i, resource in enumerate(to_download):
    print(f"({i + 1}/{len(to_download)}) Downloading {resource} and converting to webp...")
    r = requests.get(resource)
    memfile = io.BytesIO(r.content)
    im = Image.open(memfile)
    fname = resource.split("/")[-1]
    base, ext = os.path.splitext(fname)
    output_fpath = os.path.join(card_image_output_dir, base + ".webp")
    im.save(output_fpath, "WEBP")
