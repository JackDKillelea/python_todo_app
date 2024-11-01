print("Hello, thank you for using my todo list!")

while True:
    userAction = input("Type add, show, edit, delete, complete or exit: ")
    match userAction.lower().strip():
        case "add":
            userInput = input("Enter a todo: ") + "\n"
            # Read what is currently in the file and create a list from it
            todoFile = open("files/todos", "r")
            todoList = todoFile.readlines()
            todoFile.close()

            capitalised = userInput.title()
            todoList.append(capitalised)
            # Writes data to a local text file
            todoFile = open("files/todos", "w")
            todoFile.writelines(todoList)
            todoFile.close()

        case "show" | "display":
            todoFile = open("files/todos", "r")
            todoList = todoFile.readlines()
            todoFile.close()

            if not todoList:
                print("You have no current todos.")
            else:
                for index, item in enumerate(todoList):
                    row = f"{index + 1}. {item}"
                    print(row.replace("\n", ""))

        case "edit":
            todoFile = open("files/todos", "r")
            todoList = todoFile.readlines()
            todoFile.close()

            edit = int(input("Please enter the number of the item you'd like to edit: "))
            newTodo = input("Please enter updated todo: ")
            todoList[edit - 1] = newTodo

            todoFile = open("files/todos", "w")
            todoFile.writelines(todoList)
            todoFile.close()

        case "delete" | "complete":
            todoFile = open("files/todos", "r")
            todoList = todoFile.readlines()
            todoFile.close()

            if userAction.lower().strip() == "complete":
                todo = int(input("Please enter the number of the item you'd like to complete: "))
            else:
                todo = int(input("Please enter the number of the item you'd like to delete: "))
            todoList.pop(todo - 1)

            todoFile = open("files/todos", "w")
            todoFile.writelines(todoList)
            todoFile.close()

        case "exit":
            break

        case _:
            print("You entered and unknown command, please enter a valid command.")

print("Thank you. Goodbye")
