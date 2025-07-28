import os
import json

base_path = "collections"
output_json = {"collections": []}

for collection in sorted(os.listdir(base_path)):
    collection_path = os.path.join(base_path, collection)
    if not os.path.isdir(collection_path):
        continue

    collection_entry = {
        "collection_name": collection,
        "documents": []
    }

    for file in sorted(os.listdir(collection_path)):
        if file.endswith(".pdf"):
            pdf_name = os.path.splitext(file)[0]
            json_file_path = os.path.join(collection_path, f"{pdf_name}.json")
            if os.path.exists(json_file_path):
                with open(json_file_path, "r", encoding="utf-8") as jf:
                    extracted_data = json.load(jf)
            else:
                extracted_data = {}

            collection_entry["documents"].append({
                "document_name": file,
                "extracted_data": extracted_data
            })

    output_json["collections"].append(collection_entry)

# Save final output JSON
with open("challenge1b_output.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent=2)