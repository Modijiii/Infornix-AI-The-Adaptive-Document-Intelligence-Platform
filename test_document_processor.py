"""Test script for document processing pipeline."""
import sys
from pathlib import Path
from src.document_processor import DocumentProcessor

def test_processing(image_path: str):
    """Test document processing on a sample image."""
    print(f"Processing document: {image_path}")
    print("-" * 60)
    
    processor = DocumentProcessor()
    
    try:
        result = processor.process_document(image_path)
        
        print("\n" + "=" * 60)
        print("PROCESSING RESULTS")
        print("=" * 60)
        print(f"\nDocument Type: {result.get('document_type', 'Unknown')}")
        print(f"Confidence Score: {result.get('confidence_score', 0.0):.2%}")
        print(f"\nDecision: {result.get('decision', 'Unknown')}")
        print(f"\nReasoning: {result.get('reasoning', 'N/A')}")
        
        print(f"\nExtracted Fields:")
        for key, value in result.get('fields_extracted', {}).items():
            print(f"  - {key}: {value}")
        
        if result.get('anomalies'):
            print(f"\nAnomalies Detected:")
            for anomaly in result['anomalies']:
                print(f"  - {anomaly}")
        
        print(f"\nExplainability Maps:")
        print(f"  - Heatmap: {result.get('explainability_map', 'N/A')}")
        print(f"  - Field Visualization: {result.get('field_visualization', 'N/A')}")
        print(f"  - Decision Visualization: {result.get('decision_visualization', 'N/A')}")
        
        return result
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        test_processing(image_path)
    else:
        print("Usage: python test_document_processor.py <image_path>")
        print("Example: python test_document_processor.py data/sample_invoice.png")

