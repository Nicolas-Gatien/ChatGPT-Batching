# ChatGPT Batching
ChatGPT allows for batch messages -> you can start a batch job to respond to a multitude of prompts simultaneously.

The scripts in this repository facilitate that process.

# Config Folder
## Settings
Open the `config.json` file.

- model -> the OpenAI model that will be prompted.
- system-prompt -> will be used as instructions for how the model should respond to each message in the batch.
- openai-key -> paste your API key in this parameter.

## Messages
Open the `messages.txt` file.
Each line in that text file will be turned into a prompt fed into ChatGPT.
Put as many prompts as you would like, with a line break between each one.

# Using the Scripts

Step #1: Run `create_batch.py` -> this will create a batch job using the messages in the `messages.txt` file.

Step #2: Periodically run `retrieve_batch.py` -> if the batch is done processing, it will create the `output.jsonl` file, otherwise, it will print its current status.

Step #3: View `output.jsonl` when the batch is complete to view the responses.

