wordCount = int(input())

for i in range (wordCount):
    word = str(input())
    wordLength = len(word)
    if wordLength>10:
        print(word[0]+str(wordLength-2)+word[-1])
    else:
        print(word)