#1. NO parameter, NO return
def greet():
    print("Hello World!!!")
greet()

#2. No parameter , return value
def greet():
    return "Hello World!!"
print(greet())

#3. Parameter , no return
def add(a,b):
    print("Sum is ",a+b)
add(3,5)

#4. Parameter , Return value
def add(a,b):
    return a+b
result=add(5,2)
print(result)

#5. lamda function
add=lambda a,b:a+b
print(add(5,4))

