sym = [
    '!', '"', '#', '$', '%', "'", '&', '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
]
user_input = input("Input: ")
my_word = []
temp_word = []

for char in user_input:
    if char not in sym:
        temp_word += char
    elif char in sym:
        wrd = "".join(temp_word).lstrip()
        my_word.append(wrd)
        temp_word = []
if temp_word:
    wd = "".join(temp_word).lstrip()
    my_word.append(wd)

print(my_word)