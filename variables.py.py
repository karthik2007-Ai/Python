a="hi"#string
b=2 #integer
B=2.1#float

print(type(a))
print(type(b))
print(type(B))

#b and B are different because they are case sensitive

a='bye'
print(a)#it will come bye because the new assign value of a is 'bye' 

c="hi"#double quotes
c='hi'#single quotes
print(c)#both are equal 

print(int(B))
print(float(b))
print(str(b))
#print(int(a))#error because string can not change into int

mycodegoeshere=10
print(mycodegoeshere)#you can give so many characters in a variable but you should not give like this

mcgh=10
print(mcgh)#now it is easy to write again when you want

myCode=2#camel case
MyCode=2#pascel case 
my_code=2#snake case 

#you cannot give variable name as you want it has some rules

a,b,c ="hi","no hi","bye"
print(a)
print(b)
print(c)#multiple values to multiple variables

a,b,c="hii"
print(a)
print(b)
print(c)#it prints one one characters

a=b=c="hi"
print(a)
print(b)
print(c)#it prints hi for every variable 

values=["hi","not hi","not"]
x,y,z=values
print(x)
print(y)
print(z)#unpacking

x="good"
print("karthik is"+" "+x)

x=2
y=4
print(x+y)# 

x="hi"
y="bye"
z= x+" "+y#it is better to assign your answer to another variable insted of direct calling
print(z)

x="all"#global variable can be used inside a function also

def MyFun():
    print("hi"+" "+x)
MyFun()

def hi():
    x="hi"
    print(x)#only inside a function
hi()

def bye():
    global x #for inside programm and outside programm and if you want to change globle variable also
    x="hi"
bye()

print(x+" "+"all")#see it comes outside function also

name="karthik"
age=14
salary=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print("his name is",name)
print("his age is",age)
print("his daily salary is",salary)#it is better to use (',')  'comma' than ('+') plus
