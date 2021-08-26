#Slicing- access the items in a certain range
#SYntax- [left index : right index-1 : step size ]



print("Added a new line")

#for loop (Infinite loop)-

#SYntax: for iteration_variable membership_operator(in/not in) sequence(list,string,array, dictionary):
    #body of for


# for i in x: 
#     print("list elements are" , i)
# print("The list has ", len(x) , "elements")

# x=[1,2,3,4,5,6]

#range(len(x)) -- > range(6) -> 0,1,2,3,4,5
# for i in range(len(x)): 
#     if i%2==0:
#         x[i]=x[i]**2
#     else:
#         x[i]=x[i]**3
# print(x)


# sum=0
# for val in range(5):
#     sum=sum+val
# print(sum)


# for i in range(3): #0,1,2 
#     for x in range(10,14): #10,11,12,13 
#         for j in range(100,103):
#             print(i,x,j)


#range--> range(starting element, ending element-1, step size)
#range(100) --> range(0,100)




#Tuple --> Static list (Immutable) -> () 
#find out the difference between tuple and list

#String --> Immutable


# list1=[1,2,3,411,11,3,5,6,22]
# new_list=[]
# for i in list1:
#     if i%2==0:
#         new_list.append(i)
# print(new_list)

# #reverse a string
# string1="ConsuladdTraining"
# new = " "
# index=len(string1)
# while index>0: 
#     new += string1[index-1] #string1[12] -> gn
#     index=index-1    #12 11
# print(new)



#Dictionary: (Mutable)

#key -> value
#k1 -> v1
#k2 -> v2

# Syntax:  dict= {key:value, k2:v2, k3:v3 }

#keys--> unique,any data type  value--> repeated, same

#key-> name, age, salary
#value-> "yashika", 24, 476281


#n=5 --> {1:1 ,2:4 ,3:9 ,4:16 ,5:25}

# n=int(input("Enter the number"))

# d=dict()
# for i in range(1,n+1):  #range(1,6) #1,2,3,4,5
#     d[i]=i*i 
# print(d)


#s=Consultadd1234 


s=input("Enter the sentence")
d={"Digits":0,"Letters":0}
for i in s:
    if i.isdigit():
        d["Digits"]+=1 
    elif i.isalpha():
        d["Letters"]+=1
    else:
        pass #executes nothing
print("Letters", d["Letters"])
print("Digits", d["Digits"])

#Occurence of characters in a string
#s="aabccddaee"

#{a:2,b:1,c:2,d:2,e:2}
#sets-(Mutable) --> union, intersection

#frozenset-Immutable


#Mutable --> list, dictionary, set
#Immutable --> tuple, frozenset, string













