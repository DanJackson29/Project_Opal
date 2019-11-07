import pickle


def myMethod(first, second, third):
    print(first)
    print(second)
    print(third)


lst = (1, 2, 3)
myMethod(*lst)
