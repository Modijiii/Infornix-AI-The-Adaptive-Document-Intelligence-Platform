"""Prepare and cache models locally into the models/ directory."""
from src.model_manager import ensure_default_models, ensure_ner_model
from src.config import MODELS_DIR

if __name__ == "__main__":
	print("Preparing models in:", MODELS_DIR)
	ensure_default_models(download_heavy=False)
	local_ner = ensure_ner_model()
	print("NER model cached at:", local_ner)
	print("Done.")
