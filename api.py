from huggingface_hub import InferenceClient
import os

def extract_entities(text):
    # Get API key from environment variable for security
    api_key = os.getenv("HF_API_KEY")
    
    if not api_key:
        return [{"error": "API key not configured. Please set HF_API_KEY environment variable."}]
    
    client = InferenceClient(api_key=api_key)
    
    try:
        result = client.token_classification(
            text,
            model="dslim/bert-base-NER"
        )
        
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
