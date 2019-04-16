import sys # the module sys to read from system

chars =0 # a variable to count chars starting by 0
vowels = 0
Cons = 0

text = sys.stdin.read() # a variable to read from the systm
for c in text: # looping the content being read
	lines = len(text.splitlines()) # this varibale counts lines by using the function splitlines.

	if c.isalpha(): # telling the program to check if the character is alphabetic, if so:
		chars +=1 # the varable chars will add one each time the programfinds an alphabetic item.

	tokens = len(text.split()) # counting the tokens by counting the number of spaces.
for v in text:
    if v.isalpha() and v in 'aeiuoAEIUO': # to count vowels
        vowels += 1
    else:
        if v.isalpha() and v not in 'aeiuoAIUOE': #to count consonants
            Cons +=1
print( "Number of lines: ", lines , "\n number of tokens: ", tokens, "\n number of characters: ", chars, "\n Number of vowels: ", vowels, "\n Number of consonants: ", Cons, "\n average of syllables per word", chars/vowels) #telling the program to output the results.

print ('Well, counting syllables by assuming there number with orthographic vowels may not be accurate for two reasons: \n first, some syllables consist of more than one vowel, as in "play". Second, syllable may also be representd by (-vowel) sounds, as y in: my. Thus, I think we need to be careful in counting syllables this way and seek a more accurate approach.' )
