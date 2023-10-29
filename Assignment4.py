#Basic Form
#Comes Handy in normal use cases such as for constants, variables, etc.

pi=3.14
r=int(input("Enter radius : "))
print("Area is ",pi*r**2)

# Tuple Assignment 
#Useful when initializing more than 1 variable, We can also use it to swap values of 2 variables.

a, b= 5, 10
a,b = b, a #swap values
print("a= ",a," b= ",b)

# List Assignment
#Assigning values in one list to variables in another list.

nums = range(2,10,3) #list of numbers starting with 2 till 10 with gap of 3
[a,b,c]= nums
print(a)
print(b)
print(c)

#  Multiple target assignment:
#Assign values of different variables at once if they have the same values initially.

a=b=1
b=3
print(a)
print(b)

# Note that even if we changed the value of b, the value of a remains the same.

# Augmented assignment:

#It makes code more user-friendly when using things like multiple increments, multiplication. It comes useful while in loops(while, for etc)

i=1
while i<100:
  print(i)
  i*=2


