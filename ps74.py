import streamlit as st
import functions

todos = functions.get_todos()

def add_todo() :
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("My to do list")
st.write("select the todo")

for index,todo in enumerate(todos) :
    checkbox = st.checkbox(todo,key=todo)
    if checkbox :
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="todo :",placeholder="new todo",
              on_change=add_todo,key="new_todo")
