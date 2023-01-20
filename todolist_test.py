todo_list = []

while True:
    task = input("Enter a task or 'q' to quit: ")
    if task == 'q':
        break
    todo_list.append(task)

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(todo_list):
        print("{}. {}".format(i+1, task))
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Done")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a task: ")
        todo_list.append(task)
    elif choice == '2':
        task_index = int(input("Enter the task number to remove: "))
        if task_index > 0 and task_index <= len(todo_list):
            del todo_list[task_index - 1]
        else:
            print("Invalid task number.")
    elif choice == '3':
        task_index = int(input("Enter the task number to mark as done: "))
        if task_index > 0 and task_index <= len(todo_list):
            todo_list[task_index - 1] = todo_list[task_index - 1] + " (done)"
        else:
            print("Invalid task number.")
    
