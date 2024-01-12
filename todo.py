def get_todos(filepath="todo.txt"):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg,filepath="todo.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#default argument
while True:
    user_action = input("Type add or show or edit or complete or exit\n")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            if 0 <= number < len(todos):
                nv_todo = input("Enter a new todo: ")
                todos[number] = nv_todo + "\n"
                write_todos(todos)

            else:
                print("Invalid todo number.")
        except ValueError:
            print("Invalid input format. Please enter a valid todo number.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(input("Enter the number of todos to complete: "))
            todos = get_todos()

            if 0 < number <= len(todos):
                index = number - 1
                todo_to_remove = todos[index].strip("\n")
                todos.pop(index)
                write_todos(todos)
                message = f"Todo {todo_to_remove} was removed from the list."
                print(message)
            else:
                print("Invalid todo number.")
        except ValueError:
            print("Invalid input format. Please enter a valid todo number.")

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print("Goodbye!")
