from openai import OpenAI
import json
import jsonlines

config = json.load(open("config/config.json"))
client = OpenAI(api_key=config["openai-key"])

# Creates JSON Lines File Based on Messages in config/message.txt
with open("batch.jsonl", "w") as batch_file:
  with open("config/messages.txt", "r") as messages:
      i = 1
      for msg in messages:
          batch_file.write(f"""{{"custom_id": "request-{i}", "method": "POST", "url": "/v1/chat/completions", "body": {{"model": "{config["model"]}", "messages": [{{"role": "system", "content": "{config["system-prompt"]}"}},{{"role": "user", "content": "{msg.strip()}"}}],"max_tokens": 1000}}}}\n""")
          i += 1
      print(f"Loaded {i} messages into a JSONL file for batching.")

# Create OpenAI Batch File
print("Creating Batch File...")
batch_input_file = client.files.create(
  file=open("batch.jsonl", "rb"),
  purpose="batch"
)
print(f"Batch file created: {batch_input_file.id}")

print("Saving batch...")
batch_details = client.batches.create(
    input_file_id=batch_input_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
      "description": "nightly eval job"
    }
)

with open(r"batch_ids.txt", "a") as file:
    file.write("\n" + batch_details.id)
print("Batch ID Saved")