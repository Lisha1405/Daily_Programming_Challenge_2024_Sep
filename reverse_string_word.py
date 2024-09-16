def reverseWords(string):
    words =string.split()
    reversed_words = []
    for i in range(len(words)-1, -1, -1):
        reversed_words.append(words[i])

    return ' '.join(reversed_words)

string = ['the sky is blue',  "  hello world  ",  "a good   example", "    ","word"]
i=0
while i<4:
    print(reverseWords(string[i]))
    i+=1
    

