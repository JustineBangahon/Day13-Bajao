pref = ["un", "re", "pre"]
suf = ["ful", "less"]
sub = []
temp = []
wah = []
usr_inpt = input("input: ").lower()

for char in usr_inpt:
    temp += char
    tmp_j = ''.join(temp)
    wah.append(tmp_j)
    if tmp_j in pref:
        hash = '#'
        sub.append(tmp_j)
        temp = []
        tmp_len = len(tmp_j)
        tmp_j = hash * tmp_len
        temp.append(tmp_j)
    else:
        wah.append(tmp_j)

if wah:
    sub.append(tmp_j)
        

print(sub)