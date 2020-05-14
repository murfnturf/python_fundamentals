'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

sentence = str(input("Type what you would like translated into Pig Latin: "))

print(sentence)

new_s = sentence.split(', ')

for word in new_s:
    result = (word[1:] + word[0] + "ay")
    print(result)

print(new_s)