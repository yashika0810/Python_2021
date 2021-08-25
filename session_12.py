#generators - normal function 
#generators- yield keyword, can use yield more than 1 time, pauses the function and then return the value
#functions- return keyword, cannot use return more than one time, exits the program


#Internal working of a for loop--> 
#1) Iter() , Next(), StopIteration


#decorators  - add some functionality to function, provide extra functionalities
#functions are taken as arguments into another function
#def func(func2) --> func--> decorator



# def decorator(func1):  
#     def inner_function():  #wrapper function/inner
#         print("This is before function execution")
# #         x=int(input("enter value of x"))
# #         y=int(input("enter value of y"))
# #         result=x+y
# #         func1() 
# #         print(result)
# #         print("This is after execution")
# #     return inner_function

# # @decorator
# # def need(): 
# #     print("Hello I need to be decorated")

# # @decorator
# # def need2():
# # #     print("Another line added")

# # # need=decorator(need)
# # # need()
# # # need2()


# # #class- attributes --> variables, behaviour--> methods
# # #Employee - first name, dept, salary   ]

# # #syntax- 
# # #class <nameofclass>:


# # class employee:
# #     def name(self,firstname,lastname):
# #         print("These are my names")
    
# # obj=employee()
# # obj.name("Yashika","Khatri")



# # class employee:
# #     def name(self, firstname, lastname):
# #         self.firstname=firstname
# #         self.lastname=lastname
    


# # class candidate:
# #     def check(self,par1, par2):
# #         return par1+par2
# # # obj1=candidate()
# # # print(obj1.check(1,2))

# # class programmer:

# #     name="Yashika"
# #     age=25

# #     def work():
# #         print("work on application development")

# #     def __init__(self,name,testno):
# #         self.name=name
# #         self.testno=testno

# #     def customfunc(self):
# #         print("coming from customfunc, my name is", self.name)


# class Manager:

#     def work():
#         print("working on Jira")

# # obj2=Manager("yashika","10")
# # print(obj2.name, obj2.testno)
# # print(obj2.customfunc())


# #Inheritance: 

# class consultadd:   #parent/super/base class
#     def __init__(self, domain):
#         self.domain=domain
    
#     def getname(self):
#         return self.domain

#     def candidateattend(self):
#         return False


# class pcandidate(consultadd):   # child

#     def candidateattend(self):
#         return True


# c=consultadd("Python")
# print(c.getname(), c.candidateattend())
# p=pcandidate("Java")
# print(p.getname(), p.candidateattend(), p.work())


#polymorphism 

class candidate:
    def domain(self):
        print("I am learning Python")
    def language(self):
        print("I am a python student")
    def level(self):
        print("intermediate")

class trainer:
    def domain(self):
        print("I teach Python")
    def language(self):
        print("Python Trainer")
    def level(self):
        print("Expert")

c=candidate()
t=trainer()
c.domain()
for i in (c,t):
    i.domain()
    i.language()
    i.level()

#Method overiding

class Parent:
    def func1(self):
        print("This is my parent function")
    
class Child(Parent):
    def func1(self):
        print("This is my child function")

ob=Child()
ob.func1()

#Find out if we have access modifiers , super()
# _ --> protected, __ --> private

class Trainer:

    #private members
    __name= None
    __domain= None
    __salary = None

    def __init__(self,name,domain):
        self.__name=name
        self.__domain=domain
    #private member functions

    def __work(self):
        print("Name :", self.__name, self.__domain)

    def sleep(self):
        self.__work()

obj = Trainer("Yashika","Python")
obj.sleep()


