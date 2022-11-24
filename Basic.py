#open the file
with open('zero_one', 'r') as file:
    input = file.read()

#print(input)

#replace the zeros and ones in the numerical representation
input = input.replace('ZERO', '0')
input = input.replace('ONE', '1')
input = input.replace(' ', '') #remove additional spaces

#remove the additional spaces
input = input.strip()

print(len(input))