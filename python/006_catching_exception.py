prompt = 'enter the temperature'

#temp = float(inp)

try:
    inp = input(prompt) #if we input some junk string, an exception would occur
    temp = float(inp)
except:
    print('kindly enter a valid number')

