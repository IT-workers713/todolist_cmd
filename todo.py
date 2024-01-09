todos = []
while True :#loop (true is boolean)
    user_action = input("type add or show or edit or complete or exit\n")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("enter todo \n")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todos):
                row=f"{index+1}-{item}"# enumarate pour afficher les numeros
                print(row)
        case 'edit':
            nbr = int(input("enter le nombre de todo pour le modifier"))
            nbr = nbr-1
            newtodo = input("enter un nv todo")
            todos[nbr] = newtodo
        case 'complete':
            number=int(input("enter number of todos to complete"))
            todos.pop(number)

        case 'exit':


            break
print("Good Bye !! ")








