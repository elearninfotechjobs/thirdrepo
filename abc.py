a=1000#global
def f1():
    global a
    a=100#local
    b=200#local
    print(globals()['a'])

def f2():
    print(a)


f1()
f2()








