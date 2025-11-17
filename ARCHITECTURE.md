# System Architecture

## Overview

The Intelligent Document Understanding System is an end-to-end AI pipeline that processes unstructured documents, extracts information, performs reasoning, and provides explainable decisions.

## Architecture Components

### 1. OCR Processing Layer (`src/ocr_processor.py`)

**Purpose:** Extract text from document images

**Engines Supported:**
- **EasyOCR** (default): Deep learning-based OCR with high accuracy
- **Tesseract**: Traditional OCR engine

**Features:**
- Image preprocessing (denoising, thresholding)
- Text extraction with bounding boxes
- Confidence scoring per text block

**Output:**
```python
{
    "text": "Full extracted text",
    "text_blocks": [
        {"text": "...", "bbox": [...], "confidence": 0.95}
    ]
}
```

### 2. NLP Processing Layer (`src/nlp_processor.py`)

**Purpose:** Text preprocessing and analysis

**Components:**
- Text cleaning and normalization
- Tokenization (word and sentence level)
- Named Entity Recognition (NER)
  - spaCy (default)
  - HuggingFace Transformers (BERT-based NER)
- Key phrase extraction

**Output:**
```python
{
    "cleaned_text": "...",
    "tokens": [...],
    "entities": {"PER": [...], "ORG": [...], "LOC": [...]},
    "key_phrases": [...]
}
```

### 3. Document Classification (`src/document_classifier.py`)

**Purpose:** Identify document type (invoice, resume, report)

**Approach:**
- Keyword-based matching
- Pattern recognition (regex)
- Confidence scoring

**Classification Logic:**
- Invoice: Keywords like "invoice number", "bill to", "total", "vendor"
- Resume: Keywords like "education", "experience", "skills", "contact"
- Report: Keywords like "report", "summary", "findings", "conclusion"

### 4. Field Extraction (`src/field_extractor.py`)

**Purpose:** Extract structured fields based on document type

**Invoice Fields:**
- Invoice number, dates, vendor, amounts, tax, currency

**Resume Fields:**
- Name, contact info, education, experience, skills

**Report Fields:**
- Title, author, date, keywords, abstract

**Extraction Methods:**
- Pattern matching (regex)
- Named entity recognition
- Section-based extraction

### 5. Reasoning Engine (`src/reasoning_engine.py`)

**Purpose:** Perform intelligent decision-making

**Invoice Validation:**
- Check required fields
- Validate total calculations (subtotal + tax = total)
- Verify date consistency
- Detect suspicious amounts

**Resume Ranking:**
- Score based on completeness
- Evaluate education, experience, skills
- Match job keywords (if provided)
- Generate ranking (Excellent, Good, Average, Below Average)

**Report Analysis:**
- Assess quality and structure
- Check for key sections (title, author, abstract)
- Score completeness

**Anomaly Detection:**
- Missing critical information
- Unusual values
- Data inconsistencies

### 6. Explainability Module (`src/explainability.py`)

**Purpose:** Visualize model decisions and important regions

**Visualizations:**
1. **Attention Heatmap**: Highlights important text regions
2. **Field Extraction Map**: Shows where fields were extracted
3. **Decision Explanation**: Visual summary of decision factors

**Techniques:**
- Bounding box highlighting
- Color-coded field types
- Confidence score visualization

### 7. Main Pipeline (`src/document_processor.py`)

**Purpose:** Orchestrate the entire processing workflow

**Processing Steps:**
1. OCR extraction
2. NLP preprocessing
3. Document classification
4. Field extraction
5. Reasoning and validation
6. Anomaly detection
7. Explainability visualization

**Output Format:**
```json
{
    "document_type": "invoice",
    "fields_extracted": {...},
    "decision": "Valid",
    "confidence_score": 0.94,
    "reasoning": "...",
    "explainability_map": "..."
}
```

### 8. REST API (`src/api.py`)

**Purpose:** Expose system via HTTP API

**Framework:** FastAPI

**Endpoints:**
- `POST /api/process`: Process document
- `GET /api/files/{filename}`: Retrieve visualizations
- `GET /api/health`: Health check
- `GET /api/supported-types`: List supported types

## Data Flow

```
Document Image
    ↓
OCR Processor → Text + Bounding Boxes
    ↓
NLP Processor → Entities + Key Phrases
    ↓
Document Classifier → Document Type + Confidence
    ↓
Field Extractor → Structured Fields
    ↓
Reasoning Engine → Decision + Validation
    ↓
Explainability Module → Visualizations
    ↓
JSON Response
```

## Multi-Modal Approach

The system uses a **hybrid multi-modal approach**:

1. **Visual Processing**: OCR extracts text with spatial information (bounding boxes)
2. **Text Processing**: NLP analyzes semantic content
3. **Combined Understanding**: Spatial + semantic features used together

**Extension Path for LayoutLMv3:**
- Can replace keyword-based classification with LayoutLMv3
- Would fuse visual features (from image) + text features (from OCR)
- Provides better accuracy for complex layouts

## Technology Stack

- **OCR**: EasyOCR, Tesseract
- **NLP**: spaCy, NLTK, HuggingFace Transformers
- **ML**: PyTorch, Transformers
- **API**: FastAPI, Uvicorn
- **Visualization**: Matplotlib, PIL
- **Explainability**: Custom attention maps, SHAP/LIME (extensible)

## Performance Considerations

1. **OCR Speed**: EasyOCR is faster but requires more memory
2. **NLP Models**: spaCy is faster; Transformers are more accurate
3. **Caching**: Can cache models after first load
4. **GPU**: Optional for faster processing (EasyOCR, Transformers support GPU)

## Extensibility

### Adding New Document Types:
1. Add keywords in `document_classifier.py`
2. Create extraction method in `field_extractor.py`
3. Add reasoning logic in `reasoning_engine.py`

### Improving Accuracy:
1. Integrate LayoutLMv3 for classification
2. Fine-tune NER models on domain data
3. Add custom regex patterns for field extraction

### Adding Features:
1. RAG integration (LangChain/LlamaIndex)
2. Knowledge graph for entity relationships
3. Voice interaction layer (speech-to-text)

## Security Considerations

- File upload validation
- File size limits
- Sanitize extracted data
- Rate limiting (can be added)

## Future Enhancements

1. **Model Improvements:**
   - Fine-tune LayoutLMv3 on document dataset
   - Add Donut (OCR-free transformer)
   - Ensemble multiple models

2. **Features:**
   - Batch processing
   - Multi-language support
   - PDF parsing
   - Table extraction

3. **Deployment:**
   - Docker containerization
   - Cloud deployment (AWS Lambda, HuggingFace Spaces)
   - Model serving optimization

