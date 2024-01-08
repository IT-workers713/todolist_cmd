todos = []
while True :#loop (true is boolean)
    user_action = input("type add or show or exit\n")
    match user_action:
        case 'add':
            todo = input("enter todo \n")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break








