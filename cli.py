import modules.todo_functions as functions
import time

print(f"Hello, current date and time is {time.strftime("%b %d %Y, %H:%M:%S")}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        functions.add_todo(user_action)

    elif user_action.startswith("show"):
        functions.show_todos()

    elif user_action.startswith("edit"):
        try:
            functions.edit_todo(user_action)
        except ValueError:
            print("Please enter a number when using edit.")
            continue
        except IndexError:
            print("That todo does not exist, please use the show command to see what todos you have.")
            continue

    elif user_action.startswith("complete"):
        try:
            functions.complete_todo(user_action)
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
