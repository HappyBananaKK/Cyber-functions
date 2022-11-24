#Convert a string to binary
def string2binary(text):
    return ''.join(f"{ord(c):08b}" for c in text)
#Convert binary to string
def binary2string(text):
    return ''.join(chr(int(''.join(c), 2)) for c in zip(*[iter(text)]*8))
  
  #example 1 print(string2binary("S")) -> 01010011
  #example 2 print(binary2string("01010011")) ->S
    
 def binary2int(n)
     return int(str(n),2)
  
    #example 3 print(binary2int("01010011")) ->83
    
 def int2Binary(n):    
    return format(n,'b')
