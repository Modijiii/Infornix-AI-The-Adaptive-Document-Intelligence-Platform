"""Setup script for the document understanding system."""
import subprocess
import sys
import os

def install_requirements():
    """Install Python requirements."""
    print("Installing Python packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def download_spacy_model():
    """Download spaCy English model."""
    print("\nDownloading spaCy English model...")
    try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        print("✓ spaCy model downloaded successfully")
    except Exception as e:
        print(f"⚠ Warning: Could not download spaCy model: {e}")
        print("  You can install it later with: python -m spacy download en_core_web_sm")

def download_nltk_data():
    """Download NLTK data."""
    print("\nDownloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("✓ NLTK data downloaded successfully")
    except Exception as e:
        print(f"⚠ Warning: Could not download NLTK data: {e}")

def create_directories():
    """Create necessary directories."""
    print("\nCreating directories...")
    dirs = ["data", "models", "output", "uploads"]
    for dir_name in dirs:
        os.makedirs(dir_name, exist_ok=True)
        print(f"✓ Created {dir_name}/")

if __name__ == "__main__":
    print("=" * 60)
    print("Intelligent Document Understanding System - Setup")
    print("=" * 60)
    
    create_directories()
    install_requirements()
    download_spacy_model()
    download_nltk_data()    
    print("\n" + "=" * 60)
    print("Setup complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Create sample documents: python create_sample_documents.py")
    print("2. Start the API server: python main.py")
    print("3. Test the system: python test_document_processor.py data/sample_invoice.png")

