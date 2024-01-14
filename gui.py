import functions

import PySimpleGUI as sg
label = sg.Text("TYPE IN A TODO ")
input_box = sg.InputText(tooltip="ENTER A TODO ",key="todo")
add_button = sg.Button("ADD")

window=sg.Window("MY TODO APP",
                 layout=[[label],[input_box,add_button]],
                 font=('Times New Roman',20))


while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "ADD":
            todos = functions.get_todos()
            nv = values['todo'] + "\n"
            todos.append(nv)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break





window.close()
