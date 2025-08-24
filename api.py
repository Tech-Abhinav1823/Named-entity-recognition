from huggingface_hub import InferenceClient

def extract_entities(text):
    client = InferenceClient(
        api_key="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"
    )
    
    try:
        result = client.token_classification(
            text,
            model="dslim/bert-base-NER"
        )
        
        # Convert the result to the format expected by the template
        entities = []
        for item in result:
            if item.entity_group:  # Only include items with entity labels
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

