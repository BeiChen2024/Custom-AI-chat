```python
def validate_config(config):
    required_fields = ['api_key', 'model_url', 'model_name']
    for field in required_fields:
        if field not in config or not config[field]:
            raise ValueError(f"Missing or invalid configuration for {field}")
    
    if not config['model_url'].startswith(('http://', 'https://')):
        raise ValueError("Model URL must start with http:// or https://")
```
