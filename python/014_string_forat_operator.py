# use of format specifier
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

prompt = 'Enter your name : '
name = input(prompt)


prompt = '%s... PLease enter your age' % name
inp = input(prompt)
age = int(inp)

msg = '%s is %d years age...' %(name, age)
print(msg)
