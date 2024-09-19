import json
import requests

# Ollama Docs:https://github.com/ollama/ollama/blob/main/docs/api.md

class OllamaClient:
    # Ollama Restful API 默认托管在本地主机的端口 11434 上，但可以通过命令在启动的时候进行更改：
    # sudo -u ollama nohup env OLLAMA_HOST=192.168.110.131:8005 OLLAMA_ORIGINS=* ollama serve > /var/log/ollama.log 2>&1 &
    def __init__(self, base_url="http://192.168.110.131:8005"):
        self.base_url = base_url

    def chat_completions_create(self, model, messages, temperature=0.7):

        # /api/generate端点用于为给定的提示生成响应/完成，详细API文档请看：https://github.com/ollama/ollama/blob/main/docs/api.md
        url = f"{self.base_url}/api/generate"

        # 可以使用 requests 库 来调用 ollama 的 restful api， 具体要设置 响应头
        headers = {'Content-Type': 'application/json'}

        # 以及数据变量
        payload = {
            "model": model,
            "prompt": self._format_messages(messages),
            "stream": False,
            "temperature": temperature
        }

        try:

            response = requests.post(url=url, headers=headers, data=json.dumps(payload))

            # 如果是200，则打印响应文本，否则打印错误。
            if response.status_code == 200:
                # 可以从JSON对象中提取准确的响应文本
                response_text = response.text
                data = json.loads(response_text)
                actual_response = data['response']
                return actual_response
            else:
                print("Error:", response.status_code, response.text)

        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Failed to connect to Ollama server at {self.base_url}. "
                                  f"Make sure Ollama is running and accessible.")
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request to Ollama server at {self.base_url} timed out. "
                               f"The server might be overloaded or not responding.")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise ValueError(f"The specified model might not be available on the Ollama server. "
                                 f"Error: {str(e)}")
            else:
                raise

    def _format_messages(self, messages):
        formatted_prompt = ""
        for message in messages:
            if message["role"] == "system":
                formatted_prompt += f"System: {message['content']}\n"
            elif message["role"] == "user":
                formatted_prompt += f"Human: {message['content']}\n"
            elif message["role"] == "assistant":
                formatted_prompt += f"Assistant: {message['content']}\n"
        return formatted_prompt.strip()

    def _parse_response(self, response):
        return {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": response.get("response", "")
                    }
                }
            ]
        }