"""Main entry point for the document understanding system."""
import uvicorn
from src.api import app
from src.config import API_HOST, API_PORT

if __name__ == "__main__":
    print(f"Starting Intelligent Document Understanding API on {API_HOST}:{API_PORT}")
    print("API Documentation available at: http://localhost:8000/docs")
    uvicorn.run(app, host=API_HOST, port=API_PORT, reload=True)