#from functions import *
#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S %p")
print(now)

while True:
    user_input = input("Type add, show, edit, done or quit: ")
    user_input = user_input.strip()


    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_input.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for i, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{i + 1}. {item}")

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            number -= 1

            if number < 0:
                print("Enter a valid number")

            todos = functions.get_todos("todos.txt")

            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Enter a valid number")
            # goes back to beginning of loop
            continue

    elif user_input.startswith("done"):
        try:
            number = int(user_input[5:])
            if number < 0:
                print("Enter a valid number")

            todos = functions.get_todos("todos.txt")

            index = number - 1

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo that was removed from list: '{todo_to_remove}'"
            print(message)
        except IndexError:
            print("There is no such number")

    elif user_input.startswith("quit"):
        break
    else:
        print("Invalid input")

text = """Thank you for using this program. 
Goodbye."""
print(text)

# print("Bye")
