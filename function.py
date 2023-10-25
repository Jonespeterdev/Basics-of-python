def function1():
    print("function 1 called")
def function2():
    print("function 2 called")

if __name__ == '__main__':
    inputvar=int(input("1:FUNCTION 1\n 2:FUNCTION 2\nENTER YOUR CHOICE : "))
    if inputvar==1:
        function1()
    elif inputvar==2:
        function2()
    else:
        print("Wrong choice..s!")