from openai import OpenAI
import json

config = json.load(open("config/config.json"))
client = OpenAI(api_key=config["openai-key"])

id = ""
with open('batch_ids.txt') as f:
    for line in f:
        pass
    id = line
    
print(client.batches.retrieve(id))

output_id = client.batches.retrieve(id).output_file_id

content = client.files.content(output_id)

print(content.content)

with open("output.jsonl", 'w') as file:
    file.write(str(content.content))
