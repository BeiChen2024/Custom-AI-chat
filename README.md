# Custom AI Chatbot  

This is a customizable AI chatbot project that allows users to configure their own API keys and model endpoints.  

## Features  

- Supports custom API endpoints  
- Configurable AI model parameters  
- Simple web interface  
- Conversation history  

## Quick Start  

1. Clone the project:  
   ```bash  
   git clone https://github.com/yourusername/custom-ai-chatbot.git  
   cd custom-ai-chatbot  
   ```  

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Copy the config file and fill in your API information:  
   ```bash  
   cp config/config.example.json config/config.json  
   ```  

4. Edit the `config/config.json` file and enter your API key and model endpoint.  

5. Run the application:  
   ```bash  
   python src/app.py  
   ```  

6. Open your browser and visit `http://localhost:5000`.  

## Configuration  

Edit the `config/config.json` file:  

```json  
{  
    "api_key": "your_api_key_here",  
    "model_url": "https://api.example.com/v1/chat/completions",  
    "model_name": "gpt-3.5-turbo",  
    "temperature": 0.7,  
    "max_tokens": 150  
}  
```
