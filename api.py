from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# .env file load karo
load_dotenv()

def extract_entities(text):
    client = InferenceClient(
        api_key=os.getenv("HF_API_KEY")  # .env se key le raha hai
    )
    
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
