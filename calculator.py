n=input("how many digits u would like to give as input two or three:")
if n=="two":
    print("enter two numbers:")
    a=int(input())
    b=int(input())
    operation=input("Enter the operation u want to perfrom add,sub,multiply,divide,powers,modulo:")
    if operation=="add":
        result=a+b
        print("addition of two number=",result)
    elif operation=="sub":
        result=a-b
        print("subtraction of two numbers=",result)
    elif operation=="divide":
        result=a/b
        print("divison of two numbers=",result)
    elif operation=="multiply":
        result=a*b
        print("multiplication of two numbers=",result)
    elif operation=="powers":
        result=a**b
        print("powers of two number=",result)
    elif operation=="modulo":
        result=a%b
        print("mudulos of two numbers=",result)
    else:
        print("invalid entry:")
        exit
elif n=="three":
    print("enter three numbers:")
    a=int(input())
    b=int(input())
    c=int(input())
    operation=input("Enter the operation u want to perfrom add,sub,multiply,divide,powers,modulo:")
    if operation=="add":
        result=a+b+c
        print("addition of three number=",result)
    elif operation=="sub":
        result=a-b-c
        print("subtraction of three numbers=",result)
    elif operation=="divide":
        result=a/b/c
        print("divison of three numbers=",result)
    elif operation=="multiply":
        result=a*b*c
        print("multiplication of three numbers=",result)
    elif operation=="powers":
        result=a**b**c
        print("powers of three number=",result)
    elif operation=="modulo":
        result=a%b%c
        print("mudulos of three numbers=",result)
    else:
        print("invalid entry:")
        exit
else:
    print("invalid input:")
    exit()
new_operation=input("if u want to continue the operation on the results yes or no:")
if new_operation=="no":
    print("therefor your results for previous operations are:",result)
    exit
if new_operation=="yes":
    d=int(input("enter the number that u want to use:"))
    new_operation=input("enter the operation u want to perfrom add,sub,multiply,divide,powers,modulo:")
    if new_operation=="add":
        new_result=result+d
        print("addition of new number=",new_result)
    elif new_operation=="sub":
        new_result=result-d
        print("subtraction of new numbers=",new_result)
    elif new_operation=="divide":
        new_result=result/d
        print("divison of new number numbers=",new_result)
    elif new_operation=="multiply":
        new_result=result*d
        print("multiplication of new numbers=",new_result)
    elif new_operation=="power":
        new_result=result**d
        print("powers of new number=",new_result)
    elif new_operation=="modulo":
        new_result=result%d
        print("mudulos of two numbers=",new_result)
    else:
        print("invalid entry")
exit
