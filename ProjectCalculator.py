import math
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divi(x,y):
    if y==0:
        print("Cannot divide by zero ")
    else:
      return x/y
print("\tWelcome to the Program\t")
print("Please select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponential (X to the power of Y)")
print("6. Trigonometric (sine, cosine, tangent, secant, cosecant,cotangent)")
choice=int(input("Enter a choice for the mathematical operation from 1 to 6:------\t"))

if choice==1:
    x=int(input("Enter the First Number\t"))
    y=int(input("Enter the Second Number\t"))
    print("The Sum of the Numbers is:\t",add(x,y))
elif choice==2:
    a=int(input("Enter the number you want to subtract from\t"))
    b=int(input("Enter the number to be subtracted\t"))
    print("The Substraction of numbers is:\t",sub(a,b))
elif choice==3:
    c=int(input("Enter the First Number\t"))
    d=int(input("Enter the Second Number\t"))
    print("The Product of the Numbers is:\t",multiply(c,d))
elif choice==4:
    e=int(input("Enter the Numerator\t"))
    f=int(input("Enter the Denominator\t"))
    if f==0:
        print("Invalid, Cannot divide by Zero")
    else:
      print("The Division of the Numbers is:\t",divi(e,f))
elif choice==5:
    v=float(input("Enter the Base of the Power:-----"))
    j=float(input("Enter the Power to be applied to the base:----"))
    print("The Result of the base to the power is\t",math.pow(v,j))
elif choice == 6:
    
    print(" Select trignometric function:")
    print("  a. Sine")
    print("  b. Cosine")
    print("  c. Tangent")
    print("  d. Cosecant")
    print("  e. secant")
    print("  f. cotangent")
    print("  g. Back to main menu")
    trig_choice = input("  Enter trig choice (a/b/c/d/e/f/g):--")
    angle_degrees = int(input("Enter the Value of Angle:--\t"))
    angle_radians = math.radians(angle_degrees)
    if trig_choice=="a":
         print("The sine of the angle is:--\t",math.sin(angle_radians))
    elif trig_choice=="b":
         print("The cosine of the angle is:--\t",math.cos(angle_radians))
    elif trig_choice=="c":
         print("The tangent of the angle is:--\t",math.tan(angle_radians))
    elif trig_choice=="d":
         print("The cosecant of the angle is:--\t",math.pow(math.sin(angle_radians),-1))
    elif trig_choice=="e":
         print("The secant of the angle is:--\t",math.pow(math.cos(angle_radians),-1))
    elif trig_choice=="f":
         print("The cotangent of the angle is:--\t",math.pow(math.tan(angle_radians),-1))
    else:
         print("Enter a valid operation")
else:
    print("Invalid Input!!!, Enter a choice between 1 to 6")
            
                    
                    
                
                
                

                   
                    
                    
                    
                    
