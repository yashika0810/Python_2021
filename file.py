# a=5
# b=6
# result=a+b
# print("Heelo")
# print("result is")

#Numbers - 
#Int  , Float , Complex-(5j+4)
#Variables - x-10 --> x-10

#Operators 
#variable = left oeprand (OperTor) right operator --> expression


#Arithmetic Operator - > ( + ,- , / , *, **, //) --> P E MD 
#Comparision Operator -> True/False (==, !=, > ,< ,>=, <=)
#Assignment Operator -> (=, +=, -=, *=, /=)
#Logical Operator -> Or, and, not
#Identity operator -> is, is not 
#Membership operator --> in , not in 


#Input from user


#Multiplication by taking input by users


# y=int(input("Enter value of y"))

# result=x*y
# print("The result is", result)

#Decision Making 
#Syntax  
#if condition:
# body of if

# x=int(input("Please enter an integer"))
# if x<0:
#     if x>-5:
#         print("Result is greater than -5")
#     else:
#         print("result is less than -5")
# elif x==0:
#     print("Result is 0")
# elif x>0 and x<30:
#     print("result is positive and in the range 30")
# else:
#     print("Result is greater than 30")


#Looping--> while loop, for loop 
# start point = end point 
#For loop (Finite loop)
#while loop (Infinite loop)

# while condition:
    #body


# while True:
#     print("True")

x=10
while x>0: #10
    print(x)
    x=x-2  #9

    # condition  // True/False
    # Print statement
    # exit

    #Break - break the loop and throw out of the loop
    #Continue - Everyline written after continue will be skipped and it will reach to the first line of loop



# while True:
#     print("Enter any number but (-1) will quit the loop and -2 will keep you in a loop")

#     x= int(input("Enter the number"))
#     if x==-1:
#         break
#     if x==-2:
#         continue
#     print("I am inside the loop")

# print("I am outside the loop")


#Event contolled and count controlled loop

avg=0
total=0 #50 90
count=0 #1 2

print("Enter the grade (-1 to quit)")
grade=int(input("Enter your grades")) #50 40
while grade!=-1 and count<=4:
    total=total+grade #0+50=50+40=90
    count+=1  #0+1=1
    grade=int(input("Enter your grades"))
    # if count==4:
    #     break
avg=total/count  
print("Avg of subjects is", avg)




#Data structures vs Data type
#Data Type
# 1 ,2 , 3 --> int 
#1.2, 3.3 --> float
#'a' --> char
#"Consultadd" --> string

#[1,2,4.4,3,2,"consultadd"] --> 
#Data structure 
# List [], Tuple (), String " ", Sets { }, Dictionary { }

#List (Mutable -> That can be changed) --> Collection of elements

#Indexing-- access the values/elements of a list
#starts from 0
#positive integer
#increments by 1
#Negative index - starts from (-1) right side - decrements by 1

new_data=[]
for i in  data:
    if i>=0:
        new_data.append(i*i)
print(new_data)


