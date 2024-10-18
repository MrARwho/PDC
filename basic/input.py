a = eval (input ("Enter first number: "))
b = eval(input ("Enter second number: "))   
operation  = input ("Enter operation: ")

if operation == "+":
    print (a + b)
elif operation == "-": 
    print (a - b)
elif operation == "*":
    print (a * b)
elif operation == "/":
    print (a / b)
else:
    print ("Invalid operation")
