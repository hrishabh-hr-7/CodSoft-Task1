to_do_list = []

# add a task 
def add_task():
    task = input("Enter a task to add to the to-do list: ")
    to_do_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# view the to-do list
def view_list():
    if not to_do_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

# remove a task 
def remove_task():
    view_list()
    if not to_do_list:
        return
    try:
        task_number = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_number < len(to_do_list):
            removed_task = to_do_list.pop(task_number)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# main program 
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View the to-do list")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_list()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the to-do list program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
