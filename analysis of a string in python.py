puzzle = "THIS IS AN EXAMPLE!"

chr2freq = {}
for c in puzzle:
    if c not in chr2freq:
        chr2freq[c] = 1
    else:
        chr2freq[c] += 1

sorted_x = sorted(chr2freq.items(), key=lambda kv: kv[1], reverse = True)
print(sorted_x)
