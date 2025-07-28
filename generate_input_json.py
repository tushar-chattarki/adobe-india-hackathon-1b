import os
import json

base_path = "collections"
input_json = {"collections": []}

for collection in sorted(os.listdir(base_path)):
    collection_path = os.path.join(base_path, collection)
    if not os.path.isdir(collection_path):
        continue

    pdf_files = sorted([f for f in os.listdir(collection_path) if f.endswith(".pdf")])
    input_json["collections"].append({
        "collection_name": collection,
        "documents": pdf_files
    })

# Save the input JSON
with open("challenge1b_input.json", "w", encoding="utf-8") as f:
    json.dump(input_json, f, indent=2)