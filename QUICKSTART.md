# Quick Start Guide

## Installation (5 minutes)

### Option 1: Automated Setup
```bash
python setup.py
```

### Option 2: Manual Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download spaCy model
python -m spacy download en_core_web_sm

# 3. Create sample documents
python create_sample_documents.py
```

## Running the System

### 1. Start the API Server
```bash
python main.py
```

The API will start at: `http://localhost:8000`

### 2. Access API Documentation
Open your browser: `http://localhost:8000/docs`

### 3. Test with Sample Documents

**Using the test script:**
```bash
python test_document_processor.py data/sample_invoice.png
python test_document_processor.py data/sample_resume.png
python test_document_processor.py data/sample_report.png
```

**Using the API (curl):**
```bash
curl -X POST "http://localhost:8000/api/process" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@data/sample_invoice.png"
```

**Using Python:**
```python
import requests

url = "http://localhost:8000/api/process"
files = {"file": open("data/sample_invoice.png", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

## Expected Output Format

```json
{
  "document_type": "invoice",
  "fields_extracted": {
    "invoice_no": "INV-2025-321",
    "total_amount": "11220.00",
    "vendor": "ABC Solutions Pvt Ltd",
    "invoice_date": "01/15/2025",
    "currency": "USD"
  },
  "decision": "Valid",
  "confidence_score": 0.94,
  "reasoning": "Invoice passed all validation checks...",
  "anomalies": [],
  "explainability_map": "output/sample_invoice_heatmap.png",
  "field_visualization": "output/sample_invoice_fields.png",
  "decision_visualization": "output/sample_invoice_decision.png"
}
```

## Troubleshooting

### Issue: EasyOCR slow on first run
**Solution:** Normal behavior - EasyOCR downloads models on first use.

### Issue: spaCy model not found
**Solution:** Run `python -m spacy download en_core_web_sm`

### Issue: Tesseract not found (if using Tesseract)
**Solution:** 
- Windows: Install from https://github.com/UB-Mannheim/tesseract/wiki
- Linux: `sudo apt-get install tesseract-ocr`
- macOS: `brew install tesseract`

Or switch to EasyOCR (default) in `src/config.py`

### Issue: Import errors
**Solution:** Ensure all dependencies are installed:
```bash
pip install -r requirements.txt --upgrade
```

## Testing Checklist

- [x] API server starts without errors
- [x] Sample invoice processes correctly
- [x] Sample resume processes correctly
- [x] Sample report processes correctly
- [x] Visualizations are generated in `output/` directory
- [x] API endpoints respond correctly

## Next Steps

1. **Test with your own documents:** Upload your own invoices, resumes, or reports
2. **Customize extraction:** Modify field patterns in `src/field_extractor.py`
3. **Improve classification:** Enhance keywords in `src/document_classifier.py`
4. **Add custom reasoning:** Extend `src/reasoning_engine.py` with domain-specific rules

## API Endpoints

- `GET /` - API information
- `GET /api/health` - Health check
- `POST /api/process` - Process document
- `GET /api/files/{filename}` - Get visualization files
- `GET /api/supported-types` - List supported types

## Document Requirements

- **Supported formats:** PNG, JPG, JPEG
- **Minimum resolution:** 300x300 pixels recommended
- **Text quality:** Clear, readable text for best OCR results