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
    "model": "mixtral:8x7b-instruct-v0.1-q3_K_M",
    "prompt": "Write a proposal from my company, GreenTech Solutions, to the department of national defence. \
        We are proposing to do a study where we will simulate the effects of a 45MW solar farm on the base. \
        This will improve the resiliency of the base in extremem weather events such as hurricanes and \
        help in their objective of reducing greenhouse gas emissions for operating and maintaining their \
        buildings. GreenTech solutions proposes a 3 step study: Step 1 is to simulate the loads at the \
        base by developing archetypes of each building and building a virtual grid. Step two of the study \
        will involve studying the placement of the solar farm, the specific solar panels and the angle at \
        which the panels will be oriented. During this phase, we will determine the peak solar output and \
        size it to meet the capacity of the base. Finally in step three, we will size a battery storage \
        solution that can help retain energy during after hours so the base continues to have power when the \
        sun goes down",
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
