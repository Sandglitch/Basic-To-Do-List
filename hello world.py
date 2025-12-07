#age = int (input ("enter the age"))
"""
if age >18:
    print ("he is allowed to vote")
else:
    print("the person is not allowed to vote")
while age==18:
    print ("do the needed procedure")
    age+=age
for i in range(0):
    print(i)
for x in [1,2,3,4]:
    print (x)
if age<=0:
    print ("invalid age")
"""
"""
v =[10,12,13]
for i in v:
    print(i)
v.append (20)
print (v[1])
s={1,2,3}
print (s)
t=(10,10)
print (t)
"""
"""
student ={"name":"hello","age":18}
print (student["age"])

def add(a,b):
    c=a+b
    return c
q=add(10,10)
print(q)
"""
"""
#with open("data.txt", "w") as f:
#    f.write("Hello")
with open("hello.txt","w") as q:
    q.write("world")
with open("hello.txt","r") as w:
    print (w.read())
"""
"""
try:
    x=int(input("enter a  number"))
except ValueError:
    print("enter a correct number ")

import math
print (math.sqrt(1))
"""
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

p = Person("George")
p.greet()

class hello:
    def __init__(hello,name):
        hello.name=name
    def display(hello):
        print (hello.name)

h=hello("george")
h.display()


