# Hugging Face DialoGPT Chatbot Integration

This Python script demonstrates how to create a simple interactive chatbot using Hugging Face's DialoGPT model with the `transformers` library. It's designed for those interested in conversational AI and natural language processing, offering a hands-on experience with one of the most advanced chatbot technologies available.

## Features

- Interactive chatbot using DialoGPT.
- Integration with Hugging Face's `transformers` library.
- Customizable model selection.

## Prerequisites

Before running this script, make sure you have:
- Python 3.x installed.
- `torch` and `transformers` libraries installed. Install them using:


## Configuration

By default, the script uses the `microsoft/DialoGPT-medium` model. You can change the model by passing a different model name to the `HuggingFaceChatbot` class constructor.

## Usage

1. Clone this repository to your local machine.
2. Open your terminal and navigate to the script's directory.
3. Run the script using:
4. Begin the conversation with the chatbot by typing your message. Type 'exit' to terminate the conversation.


## Troubleshooting

If you encounter any issues:
- Ensure all prerequisites are installed.
- Check your Python version. This script requires Python 3.x.
- Verify that your internet connection is stable, as the script needs to download model and tokenizer data from Hugging Face's servers.

For more information on the `transformers` library and DialoGPT models, visit the [Hugging Face documentation](https://huggingface.co/transformers/).


