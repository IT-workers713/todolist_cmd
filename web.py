import streamlit as st
import functions
todos=functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)


todos= functions.get_todos()
st.title("todo application !")
st.subheader("this is my todo application !")
st.write("this is used to increase your productivity")


for todo in todos:
    st.checkbox(todo)


st.text_input(label="",
              placeholder="add new todo ",
              on_change=add_todo,key='new_todo')
st.session_state
