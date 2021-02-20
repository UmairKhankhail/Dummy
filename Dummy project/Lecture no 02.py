import math
#   Functions


def hello10times(b):
  a=1
  while a<=b:
    print("Hello world")
    a+=1
#hello10times(3)

def tofindpower(a,b):
    return a**b;
#print(tofindpower(2,3))

def calculate_even_odd(num):
    if num%2==0:
        val="The number is even."
    else:
        val="The number is odd."
    return val
#num=int(input("Enter the number you want to check wether it odd or even."))
#print(calculate_even_odd(num))

def printme(myvar="Yahoo"):
    print("I am using", myvar)
#print(printme("Google"))
#printme()


#    Quadric Equation

# a=int(input("Enter the value of a"))
# b=int(input("Enter the value of b"))
# c=int(input("Enter the value of c"))
def calculatequadraticformula(a,b,c):
     try:
      if (2*a)>0:
         x1=(-b+math.sqrt((b*b)-(4*a*c)))/(2*a)
         x2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) /( 2 * a)
         print("The two values of quadratic equation are: ",x1,"and",x2)
      else:
         print("The value of 4ac must be greater than 0.")
     except ValueError:
         print("Error: The value of 'b' must be greater so that negative value does not produce.")
#calculatequadraticformula(2,9,2)

#               Scope of a Variable

def scopeofvariable():
    #Now to make a local variable global we use global keyword
    global x
    x=17
    print(x)

#if we print the function so its statements will run first and wil make the value of x global then we will be able to print that global variable
# scopeofvariable()
# print(x)

lambdafunc=lambda a,b,c:a*b*c
#it executes faster than other functions
#It uses only single statement, in a single we can do multiple things
print(lambdafunc(5,8,9))

#if we are importing something and think that the name should be shorter then we can do like this:
#import math as Q


def numprint():
    x=10
    y=10
    print(x+y)
print(numprint())   #this will first print 20 and then None because first numprint function will run and will add x and y and after that print will run since numprint returns no value, hence it will print none

def decimalToBinary(n):
    return bin(n)
print(decimalToBinary(5))