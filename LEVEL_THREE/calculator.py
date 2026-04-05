def add(n,m):
    return n + m
def subtract(n,m):
    return n - m
def multiply(n,m):
    return n*m
def divide(n,m):
    return n/m

while True:
    print("CHOOSE THE OPERATION YOU WANT TO PERFORM")
    print("1: ADDITION")
    print("2: SUBTRACTION")
    print("3: MULTIPLICATION")
    print("4: DIVISION")
    print("5: EXIT")
    key=input("ENTER THE OPERATION NUMBER HERE:")

    match key:
        case "1":
            n=int(input("ENTER THE FIRST NUMBER:"))
            m=int(input("ENTER THE SECOND NUMBER:"))
            print(add(n,m))
        case "2":
            n=int(input("ENTER THE FIRST NUMBER:"))
            m=int(input("ENTER THE SECOND NUMBER:"))
            print(subtract(n,m))
        case "3":
            n=int(input("ENTER THE FIRST NUMBER:"))
            m=int(input("ENTER THE SECOND NUMBER:"))
            print(multiply(n,m))
        case "4":
            n=int(input("ENTER THE FIRST NUMBER:"))
            m=int(input("ENTER THE SECOND NUMBER:"))
            print(divide(n,m))
        case "5":
            print("THANK YOU FOR USING THIS CALCULATOR")
            break
        case _:
            print("INVALID OPERATION NUMBER, PLEASE TRY AGAIN")