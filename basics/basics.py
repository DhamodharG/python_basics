# variables
# variable name mustend should cannot start with numbers ex: 1user=23 
# variables should not be keywords

a,b,c = (1,2,3)
print(a,b,c)
'''----------------------------------------------------'''
a=10
a=b=c=20
print(a,b,c)
'''----------------------------------------------------'''
a = "myname"
print(a)
'''----------------------------------------------------'''

#DataTypes

# numeric ---> int, float, complex
# boolean ---> True or False
# Mapping ---> Dictionary
# set--------> set { }
## Sequence ---> List[], Tuple(), String ""

#numeric
'''----------------------------------------------------'''
a = 150000
print(type(a))

a = 4.5
print(type(a))
'''----------------------------------------------------'''

# string
a = "Name"
print(type(a))

'''----------------------------------------------------'''

##type conversion -> string cannot convert into int, 
## int can convert to string

'''----------------------------------------------------'''
# float to int
b = 2.9
c = int(b)
print(c)

'''----------------------------------------------------'''
# int to float
b = 2
c = float(b)
print(c)
'''----------------------------------------------------'''

'''----------------------------------------------------'''
# int to str
b = 2
c = str(b)
print(type(c))
'''----------------------------------------------------'''

#Sequence ---> list[]
'''----------------------------------------------------'''
list1 = ["a",1,9.5,1]
list2 = ["b",1,9.5]
print(list1)

#list methods
# append,extend,remove,index,count  print(listname.methodname[index])

print(list1[0]) #-----> index
print(type(list1[0]))
print(list1[1])
print(type(list1[1]))
print(list1[2])
print(type(list1[2]))

list1.append(20) #----> append
print(list1)
list1.append(list2)
print(list1)
print(len(list1)) #---> len
print(list1)
print(list1.count("a")) #--------->count
print(list1.count(1))
## print(list1[4][0]) # ----------> main

list1.insert(1, 4725) # ------------> insert ( position number, value )
print(list1)

'''----------------------------------------------------'''

# Tuple() --> we cannot add elements into tuples at particular position

a = ()
print(type(a))

a = (4, 7, 2 , 5)
print(a*5) #--------> repetation

a = (4, 7, 2 , 5)
print(a+a) #---> adding
print(4 in a) #---> membership
print(min(a), max(a), sorted(a))
print(sum(a))

'''----------------------------------------------------'''
# String "" ----> strings '',"",''' '''
# upper, lower, spilt, startwith, endwith, count, strip, format

s = 'My'
s1 = "Name's"
s2 = '''contain how many letters'''
print(s)
print(s1)
print(s2)
s3=s2.count("a")
print(s3)
print(s2.strip())
print(s2.split()) #----------> convert string into list
print(s2.upper())
print(s2.lower())
print(s2.startswith(('c',)))
print(s2.endswith(('r',)))
print(s2.replace("how", "----------------"))

'''----------------------------------------------------'''

# set {}
# set has no index, not allow duplicates, perform union,differe, subset and many more

a = {1,1,2,3,4,4}
print(a)

b = {"hi", 1 , 2, 3}
b.add("hello")
print(b)

b.update(["king"])
print(b)
b.remove("king")
print(b)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8}
s3 = {5, 6, 7, 8}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.isdisjoint (s2))
print(s1.issubset(s2))
print(s2.issubset(s3))

'''----------------------------------------------------'''

# Dictionary
# key , value

vocabulary = {"Details" : "Myprofile", "name" : "me" , "age" : 22 , "phone number": [48957626, 123546789]}
print(vocabulary.items())
vocabulary.update({"address": (1,2,1,2,3,4,8)})
print(vocabulary)
vocabulary.pop("Details")
print(vocabulary)
# print(vocabulary.clear())

for i,j in vocabulary.items():
    print(i,j)

'''----------------------------------------------------'''

#control statements
#if,elif,else and for, while

'''----------------------------------------------------'''

'''
a == b
a>=b
a<=b
a!=b
pass --> skip
'''
# a = 10
# if a>9:
#     pass

#if
'''----------------------------------------------------'''
a = 20
if a==10 and a<=10:
    print(True)
elif a==20 and a<=20:
    print("a is false")
else:
    print("a is not 10 and 20")
'''----------------------------------------------------'''


# for
'''----------------------------------------------------'''

a = 5
for i in range(1,5+1):
    if i==4:
        print("That is four")


#printing stars using for loop

a = 5
for i in range(0,5):
    for j in range(a-i):
        print("*", end=" ")
    print()

a = 5
for i in range(1,5+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


'''----------------------------------------------------'''

#while

c = 0
while c<=8:
    c+=1
    print(c)


num = 0
a = 10
while a!=0:
    num = num + 1
    print(num)
    a = int(input("Enter the number:"))
    


'''----------------------------------------------------'''

# break and continue

b = [1, 2, 3, 4, 5]

if 2 in b:
    for i in b:
        print(i)
        if i ==2:
            print("2 is continue without distrub the loop")
            continue
        elif i==4:
            print("At 4 is break is executed")
            break
        else:
            continue
            
'''----------------------------------------------------'''

# Functions

def me():
    print("My function")
me()

def functionname(name,meo):
    print("My function",name,meo)
functionname("its me","meo")

def functionname(a,b):
    return a+b 
print(functionname(1,2))

def functionname(a):
    for i in a:
        print(i)
functionname([1,2,3,4,5])


#attributary arguments
#it saved in answer in tuple
def functionname(*a):
    print(a)
functionname(1,2,4,3,5,8,2,5,21)

#Keywords arguments
#it saved in answer in dictionary

def functionname(**a):
    print(a)
functionname(name="me",age=21)


def me(*a):
    print("me",a)
me(18,23)

def me(**a):
    print("me",a)
me(a=18,b=23)

def outer():
    print("outer")
    def inner():
        print("inner")
    inner()
outer()

def me(a,b):
    if a==1:
        print("he is",a)
    else:
        print("he is",b)

# function call done in demfun.py

'''----------------------------------------------------'''

#file handling 
# open() read() write() append() r+ mode w+ mode 
#seek(0) to see from starting
'''----------------------------------------------------'''

f = open(r"C:\Users\gurra\Desktop\python\basics\filehandle.txt",mode='r')
h = f.read()
print(h)
f.close()

f = open(r"C:\Users\gurra\Desktop\python\basics\filehandle.txt",mode='w')
f.write("hello this is")
print(f)
f.close()

f = open(r"C:\Users\gurra\Desktop\python\basics\filehandle.txt",mode='a')
print(f.write(" me and also a "))
f.close()

f = open(r"C:\Users\gurra\Desktop\python\basics\filehandle.txt",mode="r+")
print(f.read())
f.write(" reseacher")
f.close()

f = open(r"C:\Users\gurra\Desktop\python\basics\filehandle.txt",mode="w+")
f.write("u not belive that there is a coffee shop")
f.seek(0)
print(f.read())
f.close()

'''----------------------------------------------------'''

#error handling
# we can write multi exceptions
# try -> to print except or error try mustend be write above except
# except --> here we can print what type of error facing
# else --> if no error occur it will be execute
# finally --> always print
'''----------------------------------------------------'''

try : 
    a = int(input("Enter your name of your age:"))
except ValueError:
    print("Enter only number")
else:
    print("Your are correct")
finally:
    print("mamboo")
