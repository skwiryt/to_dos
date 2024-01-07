import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("LightGrey5")

label_clock = sg.Text("")
label = sg.Text("Enter a todo.")
input_box = sg.InputText(tooltip="Here place a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
column_left = sg.Column([[label_clock],
                         [label],
                         [input_box],
                         [list_box],
                         [exit_button]])
column_right = sg.Column([[add_button],
                          [edit_button, complete_button]])

layout = [[column_left, column_right]]

# layout = [[label_clock],
#           [label],
#           [input_box, add_button],
#           [list_box, edit_button, complete_button],
#           [exit_button]]

window = sg.Window("Todos pythonProject",
                   layout=layout,
                   font=("Helvetica", 17))
while True:
    event, values = window.read(timeout=1000)
    label_clock.update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == sg.WINDOW_CLOSED:
        break
    print("values: ", values)
    print("event: ", event)
    print("event type: ", type(event))
    print("values['todos']: ", values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            list_box.update(values=todos)
            input_box.update("")
        case "Edit":
            try:
                old_value = values["todos"][0]
                new_value = values["todo"] + "\n"
                todos = functions.get_todos()
                index = todos.index(old_value)
                todos[index] = new_value
                functions.write_todos(todos)
                list_box.update(values=todos)
                input_box.update("")
            except IndexError:
                sg.popup("Select a todo first", font=("Helvetica", 17))
        case "Complete":
            try:
                to_remove = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(to_remove)
                functions.write_todos(todos)
                list_box.update(values=todos)
                input_box.update(value="")
            except IndexError:
                sg.popup("Select a todo first", font=("Helvetica", 17))
        case "todos":
            input_box.update(value=values["todos"][0])
        case "Exit":
            break

window.close()
