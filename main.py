
def printlist(tasks):
    i = 1
    for task in tasks:
        print(f"\n{i}:{task} ")
        i += 1


print("Welcome to the To Do List App!")
tasks = []
with open("data.txt","r") as file:
    for line in file:
        tasks.append(line.strip())

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
with open("data.txt","w") as file:
    for task in tasks:
        file.write(task + "\n")
print("added correctly")
