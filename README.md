# MY-FIRSTPROJECT
Project Title: Simple Python Terminal Based Calculator

 
Chosen Domain: Education 

Project Objective:  It will allow users to perform standard arithmetic operations as well as more advanced exponential and trigonometric calculations.

Features
Basic Arithmetic:
Addition,
Subtraction,
Multiplication,
Division

Error Handling: Includes a specific check to prevent and report division by zero.

----Advanced Math:

~~Exponential: Calculates X to the power of Y.

Trigonometric Functions: A dedicated sub-menu provides calculations for:
Sine,
Cosine,
Tangent,
Cosecant,
Secant,
Cotangent

User-Friendly Input:

The main menu is clear and number-driven.

The trigonometry sub-menu is letter-driven.

All trigonometric functions correctly accept the angle input in degrees and convert it to radians for calculation.

Technology Stack
Programming Language: Python

Core Module: math (used for pow, radians, sin, cos, tan)

Development Environment: VS CODE editor

High-Level Architecture

The program's logic is straightforward and built on two main concepts: functional modularity and conditional control flow.

1. Modular Design
The core arithmetic operations are separated into small, reusable functions:

add(x, y)

sub(x, y)

multiply(x, y)

divi(x, y)

This approach keeps the main part of the program clean and easy to read.

2. Control Flow
The program first prints the main menu and prompts the user for a choice from 1 to 6.

A primary if/elif/else block directs the program based on this main choice.

If Choice 6 (Trigonometric) is selected, the program enters a nested if/elif/else block to handle the sub-menu choices (a-g).

Any input outside the valid range (e.g., 7, or 'h' in the sub-menu) is caught by a final else statement, which prompts the user to enter a valid choice.

Key Implementation Details

math Module: 

This script heavily leverages Python's built-in math module. math.pow() is used for the exponential function, and math.radians() is used to convert user-friendly degree input into radians, which is required by math.sin(), math.cos(), and math.tan().

Reciprocal Functions: Cosecant, Secant, and Cotangent are calculated using their reciprocal identities. For example, Cosecant is calculated as 1 / math.sin(angle_radians), which is implemented as math.pow(math.sin(angle_radians), -1).

Type Conversion: The script uses int() and float() to correctly convert the user's string input from the input() function into numbers that can be used for calculation.

Testing Strategy
The program was tested with a variety of inputs for each of its operations:

Arithmetic: Tested with positive numbers, negative numbers, and zero.

Division: The division-by-zero check was explicitly tested by entering 0 for the denominator, which correctly printed the error message.

Trigonometry: Functions were validated against known mathematical values (e.g., cos(60) returned 0.5, sin(90) returned 1.0).

Invalid Input: The main menu was tested by entering a choice of 8, which correctly triggered the "Invalid Input" message.
# CODE


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
        
        trig_choice = input("  Enter trig choice (a/b/c/d/e/f):--")
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
            
                    
                    
                
                
                

                   
                    
                    
                    
                    
