# the welcome greeting
print("Welcome to moon time! How can I help?")

def get_help_response(value):
    if 'abuse' in value:
        collect =input("Would you like to review or collect evidence? Here are some laws regarding the issues and available shelters.")
        if collect == "yes":
            print("Providing report on evidence...")
        else:
            print("No problem! Will that be all assistence needed for today?")
    elif 'crimson tide' in value:
        print("SOS has been signaled!")
    elif 'legal advise' in value:
        legal_advisory = input("Based on chats from past situations, here are some legal laws available in SOuth Africa...{} Would you like to seek legal guidance?")
        if legal_advisory == "yes":
            print("Providing you with a professional's contact information")
        else:
            print("No problem! Will that be all assistence needed for today?")
    elif 'I would like to talk to someone' in value:
        print("Moon time is here to support and listen.")
    else:
        print("I'm sorry, I don't have information on that topic. Please ask for help on something else.")        

def get_option_input(prompt):
    while True:
        value = input(prompt)
        if value == "exit":
            print("Thank you for using the Moon Time. Goodbye!")
            break
        else:
            response = get_help_response(value)
            print(response)
            
user_input = get_option_input("You can ask for help and advise on topics and social issues or type 'exit' to end the conversation.")   