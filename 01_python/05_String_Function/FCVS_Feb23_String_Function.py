#Function
def greet():
    """
    the function prints Hi!
    """
    print('Hi')


greet()
#greet()
#greet()

def greet(name):
    print(f'Hi {name}')



greet('Asghar')

def greet(first_name, last_name):
    return f'Hello {first_name} {last_name}'

g = greet('Ali', 'Alavi')
out = g + ' welcome!'
#print(type(g))
print(out)


# open the camera! --> func_1
# take a quick photo! --> func_2
# recognize the guest! --> func_3
# say hello to the guest! --> func_4

#def welcome():
    #func_1
    #func_2
    #....
    
# Class!
# utils!
## calculate_area!
    
def multiplication(a, b, c=2):
    return a * b * c

multiplication(1, 2)


#lambda!
multiply = lambda a, b, c : a * b * c
print(multiply(3, 4, 5))


    
    



















