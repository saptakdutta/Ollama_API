# %% Libs
import requests
import json

# %% Set API parameters
# to set up docker ollama use: docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
# to download a new model use ex: docker exec -it ollama ollama run llama2:
# to check is ollama is running visit: http://localhost:11434/ in your browser

# model list:
# mixtral:8x7b-instruct-v0.1-q3_K_M
# gemma2:27b

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "applicationm/json"}
data = {
    "model": "gemma2:27b",
    "prompt": "I am going to give you some background information. Using this,can you write a program for me?",
    "stream": False,
}

# Parse the response
response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_text = response.text
    data = json.loads(response_text)
    actual_response = data["response"]
    print(actual_response)
else:
    print("Error: ", response.status_code, response.text)

# %%
