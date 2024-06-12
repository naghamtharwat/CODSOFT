def chatbot():
    print("Hello! I'm Chatbot. How can I help you today?")
    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif user_input == "hello" or "hi":
            print("Chatbot: Hello! How can I assist you today?")
        elif user_input == "how are you" :
            print("Chatbot: I'm just a bot, How about you?")
        elif user_input == "what is your name"  or "who are you":
            print("Chatbot: I'm Chatbot, your virtual assistant.")
        elif user_input == "help me please" or "help":
            print("Chatbot: Sure, I'm here to help! Please ask your question.")
        elif user_input == "weather":
            print("Chatbot: I can't check the weather right now, but you can search in weather apps.")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
