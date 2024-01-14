import functions

import PySimpleGUI as sg
label = sg.Text("TYPE IN A TODO ")
input_box = sg.InputText(tooltip="ENTER A TODO ")
add_button = sg.Button("ADD")
window=sg.Window("MY TODO APP",layout=[[label],[input_box,add_button]])

window.read()
window.close()
