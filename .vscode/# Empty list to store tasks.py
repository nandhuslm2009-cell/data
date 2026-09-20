# Empty list to store tasks
tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        # Add task
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"Added: {task}")

    elif choice == "2":
        # View tasks
        print("\n--- Your Tasks ---")
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        # Exit
        print("Bye! Good job!")
        break

    else:
        print("Wrong choice, try 1,2,3 only")