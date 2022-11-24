#since it is a multiple of 8, we can think that this is a series of
#ascii characters
result=''.join(chr(int(input[i*8:i*8+8],2)) for i in range(len(input)//8))
print(result)

#the last couple of characters are '==' ... it looks a base64
import base64
decoded = base64.b64decode(result).decode('ascii') 
#version2: decoded = base64.b64decode(result).decode('utf-8', errors="ignore")
print(decoded)

#the output is a morse code
alpha2morse = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' }

#reversing morse map
morse2alpha = {value:key for key,value in alpha2morse.items()}

#convert morse to string
decoded2 = ''.join(morse2alpha.get(i) for i in decoded.split())
print(decoded2)
