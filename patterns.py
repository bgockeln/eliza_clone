import re
# For pattern recognition

patterns = [
        (r'I feel (.*)', [
            "Why do you feel {0}", 
            "What makes you feel {0}?",
            "Do you often feel {0}?"
            ]),
        (r'My name is (.*)', [
            "Hello {0}, how can I help you today?",
            "Wow, {0} is a nice name!",
            "Wow, {0} is a shitty name, eugh!",
            "What do you want {0}?"
            ]),
        (r'(hi|hello|hey)', [
            "Hello there!",
            "Hi!",
            "Sup?",
            "Eh?"
            ]),
        (r'I m hungry', [
            "Do you want a succulent chinese meal?",
            "Me too!"
            ]),
        (r'exit', [
            "Tata and Farewell!"
            ]),
        (r'Ich fühle mich (.*)', [
            "Warum fühlst du dich {0}?",
            "Fühlst du dich oft {0}?",
            "Du fühlst dich {0}?, ist mir total egal!"
            ]),
        (r'Mir geht es (.*)', [
            "Das freut mich",
            "Hey! Super! Klasse! Ganz toll...",
            "Das interessiert mich nicht!"
            ]),
        (r'Mein Name ist (.*)', [
            "Hallo {0}, wie geht es dir?",
            "Hallo {0}, schöner Name",
            "{0}, Iggitibah was ein Name"
            ]),
        (r'Ich habe Hunger', [
            "Dann musst du dir was zu Essen machen mein lieber Freund!",
            "Ich auch!"
            ]),
        (r'ende', [
            "DOOOEIIIIII"
            ]),
        ]
        
