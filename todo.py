def display_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")
tasks=[]
while(True):
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
                task = input("Enter task: ")
                tasks.append(task)
                print("Task added successfully.")
        elif choice == '2':
                if tasks:
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task}")
                else:
                    print("No tasks.")
        elif choice == '3':
                if tasks:
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task}")
                    try:
                        idx = int(input("Enter index to edit: ")) - 1
                        if 0 <= idx < len(tasks):
                            tasks[idx] = input("New task: ")
                            print("Task edited.")
                    except ValueError:
                        print("Invalid input.")
                else:
                    print("No tasks.")
        elif choice == '4':
                # Similar to edit, but use tasks.pop(idx)
                pass  # Implement delete
        elif choice == '5':
                print("Goodbye!")
                break
        else:
                print("Invalid choice.")
        
        
        
        
        