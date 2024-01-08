todos = []
while True :#loop (true is boolean)
    user_action = input("type add or show\n")
    match user_action:
        case 'add':
            todo = input("enter todo")
            todos.append(todo)
        case 'show':
            print(todos)








