
#functions
'''
def example(x, y, z):       here, x, y, and z are "parameters"
    result = (x + y) * z
    print("The result is: " + str(result))

example(1, 2, 3):           in this form, 1, 2, and 3 are called "arguements"
                            this is referred to as "calling" a function

Output for example(1, 2, 3): The result is: 9
---------------------------------------------------------------------------------

def start(x):
    return x

def add(y, z):
    result = start(y) + z
    return result

def multiply(a, b, c):
    result = add(a, b) * c
    print(result)

start(1): Return value: 1
add(1, 2): Return value: 3
multiply(1, 2, 3): Output: 9

----------------------------------------------------------------------------------

def outerFunction(x):
    z = int(input(">> "))
    def innerFunction():   #add
        result = x + z
        print(result)
    innerFunction()

outerFunction(2)

----------------------------------------------------------------------------------

def first(value):     #print a value
    print(value)

def second(x):
    first(x)

second(2)

-----------------------------------------------------------------------------------

def add(x, y):      #add(2,2) = 4...add() = 4...bigMaths calls add()...bigMaths now has a 4
    result = x + y
    return result

def multiply(x, y):
    result = x * y
    return result

def subtract(x, y):
    result = x - y
    return result

def bigMaths(x, y, z):
    result = x * y - z
    print(result)

bigMaths(add(1, 2), multiply(2, 5), subtract(6, 2))
'''

#Arrays

oneDArray = []
#twoDArray = [[]]

def displayArray(array):
    for i in array:
        print(i)

done = False
while not done:
    displayArray(oneDArray)
    print("----------------------")
    print("[1] Add to array")
    print("[2] Pop array")
    print("[3] Quit")
    x = int(input(">> "))
    if x == 1:
        y = input("Enter something: ")
        oneDArray.append(y)
    elif x == 2:
        if len(oneDArray) > 0:
            oneDArray.pop()
        else:
            print("Array is empty! D:")
    elif x == 3:
        done = True
    else:
        print("Please..no more...options.....")
































