# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        if len(todo) <= 1:
            print("After 'add' ypu should put the todo")
            continue
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
    elif user_action.startswith("show") or user_action.startswith("display"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            newTodo = input("Ender the new todo: ")
            todos = functions.get_todos()
            todos[number - 1] = newTodo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("After 'edit' you should give the number of todo.")
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            functions.write_todos(todos)
            print(f"todo '{todo_to_remove}' was removed")
        except (ValueError, IndexError) as error:
            if type(error) is ValueError:
                print("After 'complete' you should give the number of todo.")
            else:
                print("The number was outside of the range")
    elif "exit" in user_action:
        break
    else:
        print("You entered an unknown string")

print("Bye!")
