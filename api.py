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
            # Support both dict and object style outputs
            if isinstance(item, dict):
                entity_group = item.get('entity_group') or item.get('entity') or item.get('label')
                word = item.get('word') or item.get('token') or item.get('text')
                score = item.get('score')
                start = item.get('start')
                end = item.get('end')
            else:
                entity_group = getattr(item, 'entity_group', None) or getattr(item, 'entity', None) or getattr(item, 'label', None)
                word = getattr(item, 'word', None) or getattr(item, 'token', None) or getattr(item, 'text', None)
                score = getattr(item, 'score', None)
                start = getattr(item, 'start', None)
                end = getattr(item, 'end', None)

            if entity_group and word is not None:
                entities.append({
                    'text': word,
                    'label': entity_group,
                    'score': round(float(score), 3) if score is not None else None,
                    'start': start,
                    'end': end
                })

        return entities
    except Exception as e:
        return [{"error": str(e)}]
