def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?", "how r u"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    elif user_input in ["what is your name", "what's your name?", "who are you"]:
        return "I'm a basic rule-based chatbot."
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

def run_chatbot():
    print("--- Chatbot Initialized ---")
    print("Type your message below (type 'bye' to exit):\n")
    
    while True:
        user_input = input("You: ")
        
        response = get_bot_response(user_input)
        
        print(f"Bot: {response}\n")
        
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit",]:
            break

if __name__ == "__main__":
    run_chatbot()