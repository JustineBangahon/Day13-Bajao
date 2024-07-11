user_input = input("Input: ")
words = []
tmp = ""
for w in user_input:
   if w == " ":
       words.append(tmp)
       tmp = ""
   else:
       tmp += w
if tmp:
   words.append(tmp)

print(words)

