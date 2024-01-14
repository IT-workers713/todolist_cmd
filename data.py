import PySimpleGUI as sg

label = sg.Text("enter feet")
input_text1 = sg.InputText(tooltip="enter feet")
label2 = sg.Text("enter inches")
input_text2 = sg.InputText(tooltip="enter inches")

window =sg.Window("convertor",layout=[[label,input_text1],[label2,input_text2]])

window.read()
window.close()