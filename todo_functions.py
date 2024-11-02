from data_functions import read_lines_file, write_to_file

def add_todo(user_action):
    """ Adds a todo to the local text file. """
    user_input = user_action[4:]
    todo_list = read_lines_file()
    capitalised = user_input.title()
    todo_list.append(capitalised + "\n")
    write_to_file(todo_list)

def show_todos():
    """ Shows the current todos in the local text file. """
    todo_list = read_lines_file()
    if not todo_list:
        print("You have no current todos.")
    else:
        # List Comprehension
        # formattedTodos = [item.strip("\n") for item in todoList]
        for index, item in enumerate(todo_list):
            row = f"{index + 1}. {item}"
            print(row.strip("\n"))

def edit_todo(user_action):
    """ Edits a todo in the local text file by taking in a numerical value """
    todo_list = read_lines_file()
    user_input = user_action[5:]
    print(f"You are editing: {todo_list[int(user_input) - 1]}")
    new_todo = input("Please enter updated todo: ") + "\n"
    todo_list[int(user_input.strip()) - 1] = new_todo.title()
    write_to_file(todo_list)

def complete_todo(user_action):
    """ Completes a selected todo by taking in a numerical value. """
    todo_list = read_lines_file()
    user_input = user_action[9:]
    todo_list.pop(int(user_input.strip()) - 1)
    write_to_file(todo_list)