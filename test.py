import ollama
import requests
import json

url = 'http://192.168.110.131:8005/api/generate'

headers = {'Content-Type': 'application/json'}

payload = {
    "model": "llama3.1:8b",
    "prompt": "你好",
    "stream": False,
    "temperature": 0.8
}


response = requests.post(url=url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    response_text = response.text
    data = json.loads(response_text)
    actual_response = data['response']
    print(actual_response)
else:
    print("Error:", response.status_code, response.text)

