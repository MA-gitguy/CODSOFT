#ChatBot

def simple_chatbot(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hello", "hey", "hi"]):
        return "Hi there! How can I help you?"
    elif any(word in user_input for word in ["how are you", "how was the day"]):
        return "I'm just a computer program, but thanks for asking!"
    elif any(word in user_input for word in ["your name", "name", "what is your name"]):
        return "I'm a chatbot. You can call me AbdulGPT."
    elif any(word in user_input for word in ["bye", "by", "Goodbye"]):
        return "Goodbye! If you have more questions, feel free to ask."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
