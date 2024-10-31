todoList = []

while True:
    userAction = input("Type add, show or exit: ")
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
        case "exit":
            break
        case _:
            print("You entered and unknown command, please enter a valid command.")

print("Thank you. Goodbye")
