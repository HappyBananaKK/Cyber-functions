def xor(n,m):
    y = int(n, 2)^int(m,2)
    return bin(y)[2:].zfill(len(n))

#example    print(xor("10","11")) ->01
