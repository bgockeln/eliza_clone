# Simple ELIZA Clone

A simple chatbot inspired by the classic `ELIZA` program. It talks to you by matching user input to patterns, then gives back a reply.
The patterns are stored in a seperate file called `patterns.py` so the code stays clean and the patterns are easy to change.

## How to use
1. Clone or download the project
2. run it with `python3 eliza.py`
3. Talk to `ELIZA` in the terminal
4. To quit type `quit`, `exit` or `ende`

## How it works
* The program checks the user input against a list of patterns 
* If it finds a match, it picks a random response from the options for that pattern
* If not, replies with a standard prompt: "Tell me more about that."
* it keeps going until you type an exit word. (quit, exit or ende)

## Files
* `eliza.py` - the main program
* `patterns.py` - where the chatpatterns and responses are
* `README.md` - this file

## Notes
* This is a very simple program
* Adding more patterns is easy by editing or adding entries in `patterns.py`
* Runs only in the terminal, like all great things.
