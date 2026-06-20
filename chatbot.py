# Project: Rule-Based Chatbot for CodeAlpha Internship
# Author: Vashu
# Date: June 2026

import re

def get_response(user_input):
    # Standardizing user input to lowercase and removing extra spaces
    user_input = user_input.lower().strip()
    
    # 1. Greetings
    if re.search(r'\b(hello|hi|hey|hola)\b', user_input):
        return "Hey there! I am Leo, your personal assistant. How can I help you today?"
        
    # 2. Well-being check
    elif "how are you" in user_input or "how's it going" in user_input:
        return "I'm doing great, thanks for asking! Ready to help you with your queries."
        
    # 3. About the chatbot
    elif "your name" in user_input or "who are you" in user_input:
        return "My name is Leo! I am a rule-based AI chatbot built as part of my CodeAlpha internship project."
        
    # 4. Project or Internship related queries
    elif "project" in user_input or "codealpha" in user_input:
        return "This is Task 1: A Rule-Based Chatbot. Next, I will be working on Data Analysis tasks!"
        
    # 5. Farewell
    elif re.search(r'\b(bye|goodbye|exit|tc)\b', user_input):
        return "Goodbye! Have a wonderful day ahead. Don't hesitate to reach out if you need anything else!"
        
    # 6. Default Fallback response (When no rules match)
    else:
        return "I'm not quite sure I understand that. Could you please rephrase or try asking something else?"

def main():
    print("==================================================")
    print("🤖 LEO AI CHATBOT INITIALIZED SUCCESSFULLY 🤖")
    print("==================================================")
    print("Type 'bye' or 'exit' to quit the chat.\n")
    
    while True:
        try:
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower().strip() in ['bye', 'exit', 'quit']:
                print(f"Leo: {get_response(user_input)}")
                break
                
            # Get and print response
            response = get_response(user_input)
            print(f"Leo: {response}\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\nLeo: Session ended abruptly. Goodbye!")
            break

if __name__ == "__main__":
    main()
