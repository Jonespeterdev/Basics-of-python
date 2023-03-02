
def add_2_num(firstnum,secondnum):
    answer=firstnum + secondnum #add 2 numbers got as parameter
    return answer


if __name__ == '__main__':
    #---got input from user----#
    a=int(input("Enter first number  :  "))
    b=int(input("Enter second number :  "))

    #----call `add_2_num` function with passing parameters----#
    c=add_2_num(a,b) # function the answer it stores on variable c

    print("Sum of first and second number is  :  ",c)



