def func3(arg):
    num = int(arg)
    print('inside func3() with arg')
    print(num)

def func2():
    print('inside func2()')


def func1():
    print('inside func1()')
    func2()
    func3(23)


func1()
quit()

