
# **Infornix AI — Adaptive Document Intelligence**

Infornix AI is an agentic document intelligence system that combines OCR, NLP, and autonomous reasoning to extract, classify, and validate information from complex documents. It produces structured outputs with explainable insights using confidence scoring, anomaly detection, and visual reasoning maps.

---

## 🚀 Features

* OCR-based text extraction (EasyOCR/Tesseract)
* NLP pipeline using spaCy & HuggingFace
* Document classification & field extraction
* Reasoning engine with anomaly detection
* Explainable AI (bbox maps, confidence scores)
* FastAPI microservice for scalable inference
* Sample document generator for quick testing

---

## ⚙️ Installation

```bash
git clone <repo-url>
cd infornix-ai
python setup.py
```

---

## ▶️ Usage

**Start API:**

```bash
python main.py
```

Access docs: `http://localhost:8000/docs`

**Test with a sample document:**

```bash
python create_sample_documents.py
python test_document_processor.py data/sample_invoice.png
```

---

## 📤 Example Output

```json
{
  "document_type": "invoice",
  "fields": { "invoice_number": "INV-2025-001", "total": "$1,230.00" },
  "confidence": 0.94,
  "reasoning": "Validated totals and extracted fields.",
  "explainability_map": "outputs/invoice_map.png"
}
```

---

## 🧰 Tech Stack

Python • FastAPI • EasyOCR • Tesseract • spaCy • HuggingFace • FAISS • PyPDF2 • OpenCV • Matplotlib

---

## 🔮 Future Enhancements

* LayoutLMv3 integration
* Multi-language support
* Table extraction module
* Cloud deployment

