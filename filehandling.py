#FILE: Important files: csv- .csv
# tsv - .tsv, excel, json , text, xml 

#Open, read, close, write

#Syntax: open("file_name", "working_mode")

#write- if the file is already present, it will overlap the data
#if not, create a new file automatically


#read- 
#append-

#r+ - read/write
#b- opens in binary mode
#w, r , a


#using with keyword

# with open('dat.txt', 'w') as f:
#     f.write("The file will be written")

# with open('data.txt','r') as file:
#     data=file.readline()
#     for i in data:
#         word=i.split()
#         print(word)


# try:
#     filehandler=open("da.txt",'r')
#     content=filehandler.read()
#     print(content[:20])
#     print(type(content))

# except:
#     print("Enter the correct name of your file")

# finally:
#     filehandler.close()

#argv -> helps to read command line arguments /variables from script , helps to unpack the values

from sys import argv
nameofprogram, filename = argv
print("Name of program is" , nameofprogram)
print("name of file is" ,  filename)

while True:
    try:
  
        fh=open(filename)
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        try_again=input(" The name you entered is incorrect. DO you want to try again? If yes then press Y otherwise N")

        if try_again=="Y":
            filename= input("Please enter the name correctly")
        else: 
            break
            

           
      



 