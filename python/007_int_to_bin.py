#python code to get the binary representation of an integer number

prompt = 'Enter a number :'

try:
    inp = input(prompt)
    num = int(inp)
except:
    print('Enter a valid number')


#n = 23 & (1 << 1)
#print(n)

#bin_str = None
bin_str = ''
n = 31
while n >= 0:
    if (num & (1 << n)) is not 0:
#        print('True')
        str1 = '1'
    else:
        str1 = '0'
    bin_str = bin_str + str1 + ' '
    n = n - 1

print(bin_str)
