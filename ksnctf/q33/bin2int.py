import binascii
fname = raw_input("Please input filename > ")
f = open(fname,'rb')
buffer = binascii.hexlify(f.read())
buffer1 = int(buffer,16)
print buffer1

