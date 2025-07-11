import functions
import FreeSimpleGUI as sg
import time

sg.theme('Black')

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add", size=10)
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))

complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

label2 = sg.Text("", key="label")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button, label2]],
                   font= ["Helvetica", 20])
#[] means one line on gui

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S %p"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do", font=("Helvetica", 20))


        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                # window["to-do"].update(value=f"TO-DO: {todo_to_complete} - removed... ")
                window["todo"].update(value="")
                window["label"].update(value=f"TO-DO: {todo_to_complete} - removed... ",
                                       text_color="green",
                                       font=("Helvetica", 20))
            except IndexError:
                sg.popup("Please select a to-do", font=("Helvetica", 20))

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
        # exit()

##
window.close()
