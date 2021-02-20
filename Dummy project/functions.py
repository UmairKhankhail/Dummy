import math
def cube(x):
    return x**3

def sqrt(y):
    return math.sqrt(y)

def greet(my_name):
    return "Have a great day : "+my_name
print("this statement comes in main and it always will run when ever we import a file.")

#if we have to find where the line is being executed then
#now if i say if this function is directly called then run the below lines then we use if conditon
if __name__=="__main__":
 print("This the library which we imported in online lecture no 03: "+__name__)
else:
    print("Function"+__name__+"has been called.")