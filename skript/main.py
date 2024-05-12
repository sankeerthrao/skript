from mlx_lm import load, generate

def main():
    # Load the model and tokenizer
    print("Loading the LLaMA 3 model...")
    model, tokenizer = load("mlx-community/Meta-Llama-3-8B-Instruct-4bit")
    print("Model loaded successfully.")

    # Continuously prompt for user input until 'exit' is typed
    while True:
        user_input = input("\nEnter your prompt (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        # Apply the chat template to the user input
        messages = [
            {"role": "system", "content": "You are a friendly chatbot."},
            {"role": "user", "content": user_input}
        ]
        
        print("Applying chat template...")
        input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
        prompt = tokenizer.decode(input_ids)

        # Generate a response using the LLaMA 3 model
        print(f"Generated prompt: {prompt}")
        response = generate(model, tokenizer, prompt=prompt, verbose=True)
        
        print("Response:")
        print(response)

if __name__ == "__main__":
    main()
