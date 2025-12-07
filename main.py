import json
import os
def printlist(tasks):
    i = 1
    for task in tasks:
        print(f"{i}:{task}")
        i += 1


print("Welcome to the To Do List App!")
if os.path.exists("data.json"):
    with open("data.json","r") as file:
        tasks=json.load(file)
else:
    tasks = []
x = True
while (x):
    print("Enter 1 to view tasks\nEnter 2 to add a task\nEnter 3 to exit")
    choice = int(input("Enter a choice:"))
    if choice == 1:
        printlist(tasks)
    if choice == 2:
        toappend = input("Enter the new task:")
        tasks.append(toappend)
    if choice == 3:
        print("Program was exited")
        x = False
with open("data.json","w") as file:
    json.dump(tasks,file,indent=1)
print("Added correctly")

