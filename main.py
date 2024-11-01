print("Hello, thank you for using my todo list!")

while True:
    userAction = input("Type add, show, edit, complete or exit: ")
    userAction = userAction.lower().strip()

    if 'add' in userAction or "new" in userAction:
        userInput = userAction[4:]
        # Read what is currently in the local text file and create a list from it
        with open("files/todos") as todoFile:
            todoList = todoFile.readlines()

        capitalised = userInput.title()
        todoList.append(capitalised)

        # Writes data to a local text file
        with open("files/todos", "w") as todoFile:
            todoFile.writelines(todoList)

    elif userAction == "show":
        with open("files/todos") as todoFile:
            todoList = todoFile.readlines()

        if not todoList:
            print("You have no current todos.")
        else:
            # List Comprehension
            # formattedTodos = [item.strip("\n") for item in todoList]
            for index, item in enumerate(todoList):
                row = f"{index + 1}. {item}"
                print(row.strip("\n"))

    elif "edit" in userAction:
        with open("files/todos") as todoFile:
            todoList = todoFile.readlines()

        userInput = userAction[5:]
        print(f"You are editing: {todoList[int(userInput) - 1]}")
        newTodo = input("Please enter updated todo: ") + "\n"
        todoList[int(userInput.strip()) - 1] = newTodo.title()

        with open("files/todos", "w") as todoFile:
            todoFile.writelines(todoList)

    elif "complete" in userAction:
        with open("files/todos") as todoFile:
            todoList = todoFile.readlines()

        userInput = userAction[9:]
        todoList.pop(int(userInput.strip()) - 1)

        with open("files/todos", "w") as todoFile:
            todoFile.writelines(todoList)

    elif userAction == "exit":
        break

    else:
        print("You entered and unknown command, please enter a valid command.")

print("Thank you. Goodbye")
