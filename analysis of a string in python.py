puzzle = "THIS IS AN EXAMPLE!"

puzzle = puzzle.replace(' ', '') #remove additional spaces

chr2freq = {}
for c in puzzle:
    if c not in chr2freq:
        chr2freq[c] = 1
    else:
        chr2freq[c] += 1

sorted_x = sorted(chr2freq.items(), key=lambda kv: kv[1], reverse = True)
print(sorted_x)

#change a character and print the string 
voc = {'T': 'M'}
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(dec)
