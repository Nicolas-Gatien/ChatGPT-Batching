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

## Viewing the GPT Response Messages

Step #1: After successfully running `create_batch.py` and `retrieve_batch.py`, run `save_text_responses.py` -> this will extract the text from the GPT response JSON and save to a file, should make it easy to read the responses

Step #2: View `gpt-responses.txt` to easily read the GPT-generated responses 

## Installing Requirements 

Step #1: Open terminal and change to directory **ChatGPT-Batching**
 [If you need help.](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/command-line-101)

Step #2: Run: ```pip install -r requirements.txt```

Step #3: The requirements should be installed, you're ready to use the scripts