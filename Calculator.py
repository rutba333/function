def add(P,Q):
    #This function is used for adding two numbers 
    return P+Q
def subtract(P,Q):
    #This function is used for subtracting two numbers 
    return P-Q
def multiply(P,Q):
    #This function is used for multyplying two numbers 
    return P*Q
def divide(P,Q):
    #This function is used for dividing two numbers 
    return P/Q

#now we will take inputs from the user
print("please select the operation")
print("a.addition")
print("b.subtraction")
print("c.multiplication")
print("division")
choice=input("Please choose one:a/b/c/d")
num_1=int(input("Please enter the first number:"))
num_2=int(input("Please enter the second number:"))
if choice=='a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=='b':
     print(num_1,"-",num_2,"=",subtract(num_1,num_2))
elif choice=='c':
     print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice=='d':
     print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
     print("This is an invalid input")



