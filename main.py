todoList = []

print("Hello, thank you for using my todo list!")

while True:
    userAction = input("Type add, show, edit, delete or exit: ")
    match userAction.lower().strip():
        case "add":
            userInput = input("Enter a todo: ")
            capitalised = userInput.title()
            todoList.append(capitalised)
        case "show" | "display":
            currentPos = 1
            for item in todoList:
                print(currentPos, "-", item)
                currentPos = currentPos + 1
        case "edit":
            edit = int(input("Please enter the number of the item you'd like to edit: "))
            newTodo = input("Please enter updated todo: ")
            todoList[edit - 1] = newTodo
        case "delete":
            delete = int(input("Please enter the number of the item you'd like to delete: "))
            todoList.remove(todoList[delete - 1])
        case "exit":
            break
        case _:
            print("You entered and unknown command, please enter a valid command.")

print("Thank you. Goodbye")
