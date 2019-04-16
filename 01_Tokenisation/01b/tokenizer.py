import sys
text = sys.stdin.read()
for c in text:
    if c == " ":
        text = text.replace(' ', '\n') # replacing every space to a new line so every single word will count as a token
print (text) #testing output by print to see what the program results in
