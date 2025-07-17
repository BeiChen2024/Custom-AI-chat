```python
import requests
import json

class ChatBot:
    def __init__(self, api_key, model_url, model_name, temperature=0.7, max_tokens=150):
        self.api_key = api_key
        self.model_url = model_url
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.conversation_history = []

    def generate_response(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model_name,
            "messages": self.conversation_history,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }
        
        try:
            response = requests.post(self.model_url, headers=headers, json=payload)
            response.raise_for_status()
            ai_message = response.json()['choices'][0]['message']['content']
            self.conversation_history.append({"role": "assistant", "content": ai_message})
            return ai_message
        except Exception as e:
            return f"Error: {str(e)}"
```
