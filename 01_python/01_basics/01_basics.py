#identation

age = 8

if(age < 5):
    print('He/She is a kid')


#Single Line Comment

'''
Multi 
Line
Comments!
OR 
DocString!
'''

#Continuaton of statements
a = True
b = False
c = True
if (a==True) and (b==False) \
    and (c==True):
        print('back slash')
        
        
#identifiers
variable1 = 2
_variable0 = 'Filoger'

#  1variable = True --> identifier can not starts with digits!

# @variable = 7 --> identifiers can not start with special characters!

# Var != var --> python is case sensitive!

#Object ( Scalar & Non-Scalar)

var_one = 17 #---> type:int
print('type of var_one: ' + str(type(var_one)))


var_two = 19.31 #---> type:float
print('type of var_two: ' + str(type(var_two)))

var_three = True # type:boolean
print('type of var_three: ' + str(type(var_three)))

var_four = 'TRUE' #type: string
print('type of var_four: ' + str(type(var_four)))

#Constant in python (constant does not support in python)

NUMBER_OF_STUDENTS = 30.0


#Cast (Type Conversion!)

str_sample_one = '19'

#sum_str = str_sample_one + 12
#print(sum_str)

##cast str to int - one
str_one_to_int = int(str_sample_one)
soti_type = type(str_one_to_int)
print('type of ' + str(str_one_to_int) + ' is: ' + str(soti_type))

sum_str = str_one_to_int + 12
print(sum_str)


##cast str to int - two
str_sample_two = 'Filoger'
#str_to_int_two =  int(str_sample_two)

##int to float

int_sample = 17
int_to_float = float(int_sample)

print(int_to_float)

##float to int
float_sample = 451.30
float_to_int = int(float_sample)
print(float_to_int)


##

















































            
    
    