f = open('my_file', 'w+b')
byte_arr = [120, 3, 255, 0, 100]
binary_format = bytearray(byte_arr)
f.write(binary_format)

num = 0xaabbccddeeff1122
binary_format = num.to_bytes(8, byteorder='little')
f.write(binary_format)

f.close()
