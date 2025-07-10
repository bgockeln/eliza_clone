import re
# For pattern recognition.

import random
# For random response replies

from patterns import patterns
# Importing my own pattern file.

#print(f"Loaded {len(patterns)} patterns.") #debugging

def match_input(user_input):
    """
    Handles user input by matching it to my predefined patterns.
    Returns an appropriate response if matched, otherwise "Tell me more" as default prompt.
    """
    for pattern, responses in patterns:
       # print(f"Trying pattern: {pattern} against input: {user_input}") # debugging
        # Loops through each pattern till it finds a match.
        match = re.match(pattern, user_input, re.IGNORECASE)
        # Makes the matching case-insensitive.
        if match:
            response = random.choice(responses)
            return response.format(*match.groups())
            # If the user-input matches a pattern in my pattern.py file, returns the first formatted response, for now fitting formated response
    return "Tell me more about that."
        # Return this if no matching pattern is found.

def main():
    """
    Starts the Main loop (Eliza conversation loop):
    - Greets the user
    - Prompts for input until the user types 'quit', 'exit' or 'ende' (case-insensitive)
    - Calls match_input() to generate Elizas response
    """
    print("Eliza: Hello, I am Eliza, How can I help you today? Hallo ich bin Eliza, wie kann ich dir helfen( type exit or ende to quit)")
    
    while True:
        user_input = input(">")
        # Pormpts the user with '>' and waits for input

        if user_input.lower() in ['quit', 'exit', 'ende']:
        # Ends the program if user wants to quit
            print("Eliza: Goodbye.")
            break # Stops the while loop

        response = match_input(user_input) 
        # Get Elizas response by matching user input against patterns

        print(f"Eliza: {response}") 
        # Output the response formatted with the users input if it matches

if __name__ == "__main__":
    main()
