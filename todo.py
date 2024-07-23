tasks = []


print("you are welcome to the ToDo app")
while True:
    print("\n")
    choice=int(input("pls select one of the following options\n1. Add task\n2. Delete task\n3. List tasks\n4. Quit\n Enter option> "))

    if choice == 1:
        task = input("Enter a task: ")
        tasks.append(task)
        print('task added')

    elif choice == 2:
       task_toremove = input("enter task to remove: ")
       tasks.remove(task)
       print("task removed")

    elif choice == 3:
         if not task:
             print("no tasks yet")
         else:
            print("Tasks")
         for task in tasks:
                print(task)
    elif choice == 4:
        break
    
    else:
        print('Invalid selection, pls try again')

