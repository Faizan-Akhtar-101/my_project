tasks = []  # empty list to store tasks

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":   # Add task
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":   # Remove task
        # if tasks:           Text as it is likhain gy to remove ho ga 
        #     task = input("Enter task to remove: ")
        #     if task in tasks:
        #         tasks.remove(task)
        #         print("Task removed!")
        #     else:
        #         print("Task not found!")
        # else:
        #     print("No tasks to remove!")
        tasks.clear() 
        print("Task Cleared Successfully!")

    elif choice == "3":   # Show tasks
        if tasks:
            print("Your Tasks:")
            for t in tasks:
                print("-", t)
        else:
            print("No tasks available!")

    elif choice == "4":   # Exit
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
