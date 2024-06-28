
# read output.jsonl, saves just the GPT messages to a text file for easy to read
import json

json_results = open("output.jsonl", "r").read()

f = open("gpt-responses.txt", "w+")
responses = (str(str(json_results)[2:len(str(json_results))-3])).split("\\n")
for response in responses:
    response = bytes(json.loads(response)['response']['body']['choices'][0]['message']['content'], 'utf-8')
    f.write(response.decode('unicode-escape') + "\n")
f.close()

