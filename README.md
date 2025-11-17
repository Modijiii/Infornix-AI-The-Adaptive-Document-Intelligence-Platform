
# **Infornix AI — The Adaptive Document Intelligence Platform**

Infornix AI is an agentic document intelligence system that integrates OCR, NLP, and autonomous reasoning to extract, classify, and validate information from multi-format documents. The platform delivers structured outputs with explainable AI insights through confidence scoring, anomaly detection, and visual reasoning maps.

---

## 🚀 **Features**

* **OCR Processing:** EasyOCR / Tesseract-based text extraction with bounding-box metadata
* **NLP Pipeline:** Tokenization, entity recognition (spaCy/HuggingFace), phrase extraction
* **Document Classification:** Hybrid rule-based + semantic classification
* **Field Extraction:** Regex + NER-driven extraction for invoices, resumes, reports, etc.
* **Autonomous Reasoning:** Validations, anomaly detection, decision scoring
* **Explainable AI:** Visual maps, confidence scores, field highlighting
* **API Integration:** FastAPI microservice for scalable inference
* **Sample Document Generator:** Auto-creates test docs for quick experimentation

---

## 🧠 **Architecture Overview**

```
Document → OCR → NLP → Document Classifier → Field Extraction 
        → Reasoning Engine → Explainability → JSON Output + Visual Maps
```

**Key Modules:**

* `ocr_processor` – Text + bbox extraction
* `nlp_processor` – Cleaning, NER, keyphrase extraction
* `document_classifier` – Type detection
* `field_extractor` – Structured field extraction
* `reasoning_engine` – Validations & decision logic
* `explainability` – Attention/visual maps
* `main.py` – FastAPI server
* `test_document_processor.py` – End-to-end test runner

---

## 📂 **Project Structure**

```
.
├── ARCHITECTURE.md
├── create_sample_documents.py
├── prepare_models.py
├── test_document_processor.py
├── main.py
├── setup.py
└── data/
```

---

## ⚙️ **Installation**

```bash
git clone <repo-url>
cd infornix-ai
python setup.py
```

This will:
✔ install dependencies
✔ download spaCy models
✔ create required folders
✔ prepare environment

---

## ▶️ **Usage**

### **Run API Server**

```bash
python main.py
```

Visit: `http://localhost:8000/docs` to test endpoints.

### **Run a Test on Sample Document**

```bash
python create_sample_documents.py
python test_document_processor.py data/sample_invoice.png
```

---

## 📤 **API Endpoints**

| Method | Endpoint                | Description               |
| ------ | ----------------------- | ------------------------- |
| POST   | `/api/process`          | Process a document        |
| GET    | `/api/files/{filename}` | Fetch visual explanations |
| GET    | `/api/health`           | Health check              |
| GET    | `/api/supported-types`  | Document types supported  |

---

## 🧪 **Output Example**

A typical response includes:

```json
{
  "document_type": "invoice",
  "fields": {
    "invoice_number": "INV-2025-102",
    "total": "$4,520.00"
  },
  "confidence": 0.94,
  "anomalies": [],
  "reasoning": "Amount matches computed totals.",
  "explainability_map": "outputs/invoice_map.png"
}
```

---

## 📌 **Tech Stack**

* **Python**, **FastAPI**
* **EasyOCR**, **Tesseract OCR**
* **spaCy**, **HuggingFace Transformers**
* **FAISS**, **PyPDF2**
* **Matplotlib**, **OpenCV**
* **Uvicorn**

---

## 🔍 **Key Capabilities**

* Reads both scanned + digital documents
* Extracts structured fields with high accuracy
* Performs domain-level validations
* Generates human-readable reasoning
* Provides explainability for every prediction
* Modular, scalable microservice architecture

---

## 🛠️ **Future Enhancements**

* LayoutLMv3-based deep-learning upgrade
* Multi-language support
* Table extraction module
* Cloud deployment (AWS/GCP)
* RAG integration for external knowledge validation
