import functions

import PySimpleGUI as sg
label = sg.Text("TYPE IN A TODO ")
input_box = sg.InputText(tooltip="ENTER A TODO ",key="todo")
add_button = sg.Button("ADD")
list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True,size=(45,10))
edit_button = sg.Button("EDIT")
complete_button = sg.Button("COMPLETE")
exit_button = sg.Button("EXIT")
window=sg.Window("MY TODO APP",
                 layout=[[label],[input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],
                 font=('Times New Roman',20))


while True:
    event,values=window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "ADD":
            todos = functions.get_todos()
            nv = values['todo'] + "\n"
            todos.append(nv)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "EDIT":
            todo_to_edit= values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]= new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "COMPLETE":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'EXIT':
            break
        case 'todos':
            window['todo'].update(value=values['todos'])


        case sg.WINDOW_CLOSED:
            break





window.close()
