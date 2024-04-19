'''Script for using API'''

import json
import requests

with open('input.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

response = requests.post('http://127.0.0.1:8000/predict', json=input_data, timeout=10)
data = json.loads(response.content)

print(data['total_revenue'])
