# Legends of Runeterra Cheat Sheet

This is a web app that features a filterable list of Legends of Runeterra cards.
It's pre-loaded with a list of potentially dangerous cards that your opponent should have and that you should play around, but you can also filter to show your own dangerous list.

It may still be up on http://lor.pedrovhb.com.

It's fully static and was built using Svelte and TailwindCSS. The files in `lor_sheet/card_data/orig_data` come from the Riot Games API page for Legends of Runeterra. The `process_cards` Python script then processes these files to trim down on the info (since we don't require descriptions and such) and downloads images for the cards, converting them to .webp before saving. This turns a ~750 KB image into a ~50 KB file with little quality loss!