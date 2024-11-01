def read_lines_file(file):
    with open(file) as opened_file:
        file_content = opened_file.readlines()
    return file_content

def write_to_file(file, content_to_write):
    with open(file, "w") as opened_file:
        opened_file.writelines(content_to_write)

def add_todo(user_action):
    user_input = user_action[4:]
    todo_list = read_lines_file("files/todos")
    capitalised = user_input.title()
    todo_list.append(capitalised + "\n")
    write_to_file("files/todos", todo_list)

def show_todos():
    todoList = read_lines_file("files/todos")
    if not todoList:
        print("You have no current todos.")
    else:
        # List Comprehension
        # formattedTodos = [item.strip("\n") for item in todoList]
        for index, item in enumerate(todoList):
            row = f"{index + 1}. {item}"
            print(row.strip("\n"))

def edit_todo(user_action):
        todo_list = read_lines_file("files/todos")
        user_input = user_action[5:]
        print(f"You are editing: {todo_list[int(user_input) - 1]}")
        new_todo = input("Please enter updated todo: ") + "\n"
        todo_list[int(user_input.strip()) - 1] = new_todo.title()
        write_to_file("files/todos", todo_list)

def complete_todo(user_action):
    todo_list = read_lines_file("files/todos")
    user_input = user_action[9:]
    todo_list.pop(int(user_input.strip()) - 1)
    write_to_file("files/todos", todo_list)

print("Hello, thank you for using my todo list!")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        add_todo(user_action)

    elif user_action.startswith("show"):
        show_todos()

    elif user_action.startswith("edit"):
        try:
            edit_todo(user_action)
        except ValueError:
            print("Please enter a number when using edit.")
            continue
        except IndexError:
            print("That todo does not exist, please use the show command to see what todos you have.")
            continue

    elif user_action.startswith("complete"):
        try:
            complete_todo(user_action)
        except ValueError:
            print("Please enter a number when using complete.")
            continue
        except IndexError:
            print("That todo does not exist, please use the show command to see what todos you have.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You entered and unknown command, please enter a valid command.")

print("Thank you. Goodbye")
