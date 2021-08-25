#functions --> pre-defined- add(),update(),reverse()
#user-defined 

#less no of code
#removes redundancy

#Syntax:
#def <function_name>():
    #body of function


# def func():      #function definition
#     print("Hello this is my first statement")
#     print("This is my second statement")
    
# object=func()    #function calling
# print(object)


def add():    #defining 
    x=10 
    y=20
    result=x+y
    return result
 
def sub():  #defining
    x=10
    y=20
    result=x-y
    return result

# a=add()
print(sub())
print(add())
# print(a,b)







#lamda arguments(multiple): expression(one)
def add(x,y):
    return x

obj=add(20,30)
print(obj)

x=lambda x,y:x+y
x(20,30)

#l=[1,2,3,4] -> (((10+20)+30)+40)


# def sum(num):
#     if(type(num)==int):
#         add=0
#         for i in range(1,num+1): #range= 1,7- 1,2,3,4,5,6
#             add=add+i
#         return add
#     else:
#         return 0

# op=sum(input("Enter number")
# print(op)

# s="My name is Yashika"
# a=s.split(" ")
# new_list=[]
# for i in a:
#     result =i[::-1]
#     new_list.append(result)
# print(new_list)
# print(" ".join(new_list))

# print(a)

#comma seperated values
# input_list=list(map(int, input().split(",")))
# list_len=1
# for num in range(len(input_list)-1): 
#     if(input_list[num+1]-input_list[num]==1): #input_list[1]-input_list[0] = 2-1=1
#         list_len+=1
#         continue
#     else:
#         print(input_list[num+1]) 
#         break

#Data structure comprehension
# List Comprehension -->  Syntax: [operation for i in seq]
#decision making ?? yes
#multiple if blocks?? yes
#If and else- yes 

x=[12,3,4,45]
new_list=[]
odd=[]
for i in range(len(x)):
    if i%2==0:
        new_list.append(x[i]**2) 
    else:
        new_list.append(x[i]**3)

print(new_list)

var=[i**2 if i%2==0 else i**3  for i in range(1,11)]








#Dictionary Comprehension










