import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class HuggingFaceChatbot:
    def __init__(self, model_name="microsoft/DialoGPT-medium"):                     #You can copy and paste model name from Hugging Face
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        # Fix for the padding warning
        self.tokenizer.padding_side = "left"
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.chat_history_ids = None

    def get_response(self, user_input):
        new_user_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')

        bot_input_ids = torch.cat([self.chat_history_ids, new_user_input_ids], dim=-1) if self.chat_history_ids is not None else new_user_input_ids

        self.chat_history_ids = self.model.generate(bot_input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)

        response = self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response

def main():
    chatbot = HuggingFaceChatbot()
    print("Chatbot initialized. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting chatbot.")
            break
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
