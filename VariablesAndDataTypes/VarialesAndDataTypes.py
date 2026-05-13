# Variables
# int
# float
# str
# bool
# type()
# input()
##########Variables and Data Types in Python########

a = (10 + 20) / 3
print("a is of " + str(a) + str(type(a)))
# print(type(a))
print("a value is %s is of %s type " %(a, type(a)))

b = round(3.14)
print("b is of " + str(b) + str(type(b)))

c = "Hello"
print("c is of " + c + str(type(c)))

d = True
print("d is of " + str(type(d)))

#########User Input in Python########

print("Enter your name: ")  
name = input()
print("Hello " + name)
print("Enter your age: ")
age = int(round(float(input())))

age = age + 20

print("You are " + str(age) + " years old + 20.")

print("Are you a student? (True/False):")
###########Converting user input to boolean: Can only check the presence#########
is_student = bool(input())
print("You are a student: " + str(is_student))


###########Variable Assignment and Swapping in Python#########
a= 10
b= 20.3
s = "Hello"
c = True

print("a is of %s " % a)
print("b is of %s " % b)
print("s is of %s " % s)

a, b,  c = b, a, s

print("a is of %s " % a)
print("b is of %s " % b)
print("s is of %s " % s)
print("c is of %s " % c)

#########Memeory Management in Python#########

a = [1, 2, 3]
b=a
b.append(4)
print("a is of %s " % a)

print(id(a))
print(id(b))

x = 10000000
y = 10000000

print(x == y)
print(x is y)
print(id(x))
print(id(y))

###########Arthemetic Operators in Python###########

	# +	Addition
	# -	Subtraction
	# *	Multiplication
	# /	Division
	# //	Floor division
	# %	Modulus
	# **	Power

print(  2 + 3)   # Addition
print(  5 - 2)   # Subtraction
print(  4 * 3)   # Multiplication
print(  10 / 2)  # Division
print(  10 // 3) # Floor division
print(  10 % 3)  # Modulus
print(  2 ** 3)  # Power