def read_lines_file(file):
    with open(file) as opened_file:
        file_content = opened_file.readlines()
    return file_content

def write_to_file(file, content_to_write):
    with open("files/todos", "w") as file:
        file.writelines(content_to_write)
    return

print("Hello, thank you for using my todo list!")

while True:
    userAction = input("Type add, show, edit, complete or exit: ")
    userAction = userAction.lower().strip()

    if userAction.startswith("add") or userAction.startswith("new"):
        userInput = userAction[4:]
        todoList = read_lines_file("files/todos")
        capitalised = userInput.title()
        todoList.append(capitalised + "\n")

        write_to_file("files/todos", todoList)

    elif userAction.startswith("show"):
        todoList = read_lines_file("files/todos")

        if not todoList:
            print("You have no current todos.")
        else:
            # List Comprehension
            # formattedTodos = [item.strip("\n") for item in todoList]
            for index, item in enumerate(todoList):
                row = f"{index + 1}. {item}"
                print(row.strip("\n"))

    elif userAction.startswith("edit"):
        try:
            todoList = read_lines_file("files/todos")
            userInput = userAction[5:]
            print(f"You are editing: {todoList[int(userInput) - 1]}")
            newTodo = input("Please enter updated todo: ") + "\n"
            todoList[int(userInput.strip()) - 1] = newTodo.title()
            write_to_file("files/todos", todoList)
        except ValueError:
            print("Please enter a number when using edit.")
            continue
        except IndexError:
            print("That todo does not exist, please use the show command to see what todos you have.")
            continue

    elif userAction.startswith("complete"):
        try:
            todoList = read_lines_file("files/todos")
            userInput = userAction[9:]
            todoList.pop(int(userInput.strip()) - 1)
            write_to_file("files/todos", todoList)
        except ValueError:
            print("Please enter a number when using complete.")
            continue
        except IndexError:
            print("That todo does not exist, please use the show command to see what todos you have.")
            continue

    elif userAction.startswith("exit"):
        break

    else:
        print("You entered and unknown command, please enter a valid command.")

print("Thank you. Goodbye")
