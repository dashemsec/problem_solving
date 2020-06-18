# convert str 'hello world' to 'hello_world'

gret = 'hello World'

#gret[5] = '_'
# the above commented statement is causing typeError

new_gret = gret[:5] + '_' + gret[6:]

print(new_gret)
print(len(new_gret))
