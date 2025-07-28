# Adobe Hackathon 2025 - Round 2 Challenge 1b: Multi-Collection PDF Table Extractor

This project is a solution for the Adobe India Hackathon 2025 - Round 2 Challenge 1b.  
It processes multiple collections of PDFs, extracts tabular data from each file, and compiles the results into a single output.json.

---

## 📁 Project Structure

```bash
adobe-hackathon-round1b/
├── collections/
│   ├── sample1/
│   │   ├── sample3.pdf
│   │   ├── sample5.pdf
│   │   ├── sample7.pdf
│   │   ├── sample9.pdf
│   │   └── sample11.pdf
│   ├── sample2/
│   │   ├── sample4.pdf
│   │   ├── sample6.pdf
│   │   ├── sample8.pdf
│   │   ├── sample10.pdf
│   │   └── sample12.pdf
│   └── input.json
├── output/
│   └── output.json
├── extractor/
│   └── extract_tables.py
└── README.md
---

## ⚙ How to Run

1. *Install requirements*:
   ```bash
   pip install pymupdf

2. Run the table extraction script:

python extractor/extract_tables.py collections/sample1/sample3.pdf

Output JSONs will be stored inside the respective collection folder or printed to console.


3. Input File (input.json): Located in collections/, it maps each collection and lists all PDFs inside.


4. Output File (output.json): Located in output/, it stores the extracted tabular content per PDF and per collection.

#🛠 Tech Stack

Python

PyMuPDF (fitz)

JSON



🛠 Setup Instructions

1.cd adobe-hackathon-round1b


2. Install Dependencies

pip install PyMuPDF


3. Prepare Collections

Place PDF files into subfolders inside collections/ (e.g., sample1/, sample2/, etc.)

Ensure input.json lists these collections.



4. Run the Extraction Script

python extractor/extract_tables.py


5. Check Output

The final results will be saved in output/output.json.





---

📄 Example input.json

{
  "collections": [
    {
      "name": "sample1",
      "pdfs": ["sample3.pdf", "sample5.pdf", "sample7.pdf", "sample9.pdf", "sample11.pdf"]
    },
    {
      "name": "sample2",
      "pdfs": ["sample4.pdf", "sample6.pdf", "sample8.pdf", "sample10.pdf", "sample12.pdf"]
    }
  ]
}


---

📦 Output Format (output/output.json)

Each collection includes:

collection_name: name of the folder

files: list of PDF filenames with their extracted table data (as raw text for now)



---

📌 Notes

Ensure the folder names in input.json match the subfolder names inside collections/.

This version extracts all text as-is using PyMuPDF. To extract structured tables, enhancement with ML or rule-based logic is possible.



---

🔁 Future Improvements

Add proper table structure recognition.

Support multilingual PDFs using language detection.

Use OCR for scanned PDFs (e.g., via Tesseract).