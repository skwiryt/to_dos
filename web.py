import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""
    st.write(add_input)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("Udemy Todo training App")
st.write("This is a python course training productivity app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()

add_input = st.text_input(label="", placeholder="Add a todo",
                          on_change=add_todo, key="new_todo")
