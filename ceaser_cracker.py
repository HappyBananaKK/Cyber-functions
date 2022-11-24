#Function utilized to crack ceaser cipher
def ceasar_cracker(text, from_ = -30, to_=+30):
    for i in range(from_, to_): #possible keys [-30, 30]
        #decode
        curr_step = ''.join([chr(ord(c) + i) for c in text])

        #print
        print(f"Step={i}\t{curr_step}")
#example
l=sadfahadf
ceasar_cracker(l)
