import os
import fitz  # PyMuPDF
import json

def extract_tables_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    data = {"file_name": os.path.basename(pdf_path), "tables": []}

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        if "Table" in text or "table" in text:  # basic trigger
            data["tables"].append({
                "page": page_num + 1,
                "content": text.strip()
            })

    return data

def process_collections(base_dir="collections"):
    for sample_folder in os.listdir(base_dir):
        sample_path = os.path.join(base_dir, sample_folder)
        if os.path.isdir(sample_path):
            for filename in os.listdir(sample_path):
                if filename.endswith(".pdf"):
                    pdf_path = os.path.join(sample_path, filename)
                    result = extract_tables_from_pdf(pdf_path)
                    json_path = os.path.join(sample_path, filename.replace(".pdf", ".json"))
                    with open(json_path, "w", encoding="utf-8") as f:
                        json.dump(result, f, indent=2)
                    print(f"Extracted: {pdf_path}")

if __name__ == "__main__":
    process_collections()