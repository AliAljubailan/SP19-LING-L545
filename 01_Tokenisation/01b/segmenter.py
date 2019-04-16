import sys # import the model sys to have it ready read from the system or keyboard

text = sys.stdin.read() # a variable tellin the program to read for system
for c in text: # looping the content
    if c == ".": # if an item in the content is a full stop, then
        text = text.replace(c,'\n') # modify the content by changing periods to new lines.
print (text)
        

