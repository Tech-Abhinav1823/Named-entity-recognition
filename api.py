from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

def extract_entities(text):
    # Read API key from environment
    api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN") or os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        # Fail fast if the API token is not configured
        raise ValueError("Hugging Face API token not found. Please set HUGGINGFACEHUB_API_TOKEN in your .env file.")

    model_id = os.getenv("HF_NER_MODEL", "dslim/bert-base-NER")
    
    # Initialize the client with the model and token
    client = InferenceClient(model=model_id, token=api_key)

    try:
        result = client.token_classification(text)
        
        entities = []
        for item in result:
            if item.entity_group:
                entities.append({
                    'text': item.word,
                    'label': item.entity_group,
                    'score': round(item.score, 3),
                    'start': item.start,
                    'end': item.end
                })
        
        return entities
    except Exception as e:
        return [{"error": str(e)}]
