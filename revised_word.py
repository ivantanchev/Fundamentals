word = input()
revised_word=""
for i in range(len(word)-1,-1,-1):
    revised_word+=word[i]
print(revised_word)

