##Python file: task_manager.py
# For a better output visualisation, please open this file in PyCharm, Thank you.

#=====importing libraries===========
# Datetime module imported to validade the correct format entered by the user on the 'Register New User Section'.
from datetime import date
from datetime import datetime

#=====General variables for constant use===========
# General variables declared - for text formatting as well as for 'today' date - to be used throughout the program.
RED = "\033[91m"
GREEN = "\033[92m"
WHITE = "\033[0m"
ITALIC_S = "\x1B[3m"
ITALIC_E = "\x1B[0m"
todays_date = date.today().strftime("%d %b %Y")

#====Login Section====
# Programme introduction, followed by opening the user_file, where users are enrolled on reading mode only.
# This is followed by assigning string variables to empty lists for the user and password logins.
# Read usernames and password from the file 'user.txt' using for loop, iterating through the user and password file
# Store them on the assigned list of string variables, closing the file afterwards.
# Get the username and password combination from user, validating their existence.
print("───────────────────────────────────────────────────────")
print("\t\t\t  SMALL BUSINESS TASK MANAGER")
print("───────────────────────────────────────────────────────")
# Access "user.txt" file in read mode
user_file = open("user.txt", "r", encoding='utf-8-sig')
login_user, login_pass = [], []

# Run through "user.txt" file to check for matching combination for both usernames and passwords
for line in user_file:
    username, password = (line.strip("\n").split(", "))
    login_user.append(username)
    login_pass.append(password)
user_file.close()

# Get username and password combination from user
user_name = input("Please Enter Your Username: ")
# While loops to validate the username and respective password. If the user does not enter a correspondent username or
# password, the user is notified and requested to retry.
# Validating the username.
while not user_name in login_user:
    print(f"{RED}Sorry, we can't find an account on that user name.{WHITE}\n"
          f"───────────────────────────────────────────────────────")
    user_name = input("Please Enter Your Username: ")
user_file_pos = login_user.index(user_name)
user_password = input("Please Enter Your Password: ")
# Validating the combination of the username and respective password.
while user_password != login_pass[user_file_pos]:
    user_password = input(f"{RED}Username And Password Don't Match.{WHITE}\nPlease Enter Your Password: ")


#====Main Menu Section====
# Presenting the main menu to the user and making sure that the user input is converted to lower case.
# This is followed by the main if-elif-else statement to validate the appropriate option from the menu selection.
# While loop to continue returning to menu until user selects option 'exit'.
while True:
    print(f"───────────────────────────────────────────────────────\n\t\t\t\t\t MAIN MENU\n"
          f"───────────────────────────────────────────────────────\n"
          f"[ r  ] - Register User\n"
          f"[ a  ] - Add Task\n"
          f"[ va ] - View All Tasks\n"
          f"[ vm ] - View My Tasks\n"
          f"[ e  ] - Exit")
    # Only display this menu option if 'admin' is logged in.
    if user_name == "admin":
        print(f"[ s  ] - View Overall Statistics")
    # Inform user of option to return to main menu.
    print(f"{ITALIC_S}=>Note: Please Enter '0' To Return To This Main Menu.<={ITALIC_E}\n"
          f"───────────────────────────────────────────────────────")
    menu_option = input("Please Select One Of The Above Options: \t").lower()

    # ====Register New User Section====
    # If the user enters 'r' and is an admin, they can add a new user by inputting a desired username and password.
    # The user must then confirm the password. If the passwords do not match, the user is prompted to try again.
    # Only admins are allowed to register new users.
    # If user is not authorised, they will not be given access and a message will show saying they are not authorised.
    if menu_option == "r":
        # Validating if the user is 'admin'.
        if user_name == "admin":
            print(f"───────────────────────────────────────────────────────\n\t\t\t\t REGISTER NEW USER\n"
                  f"───────────────────────────────────────────────────────")
            # Access "user.txt" file in append mode
            user_file = open("user.txt", "a+", encoding='utf-8-sig')
            # Request input of a new username to be added, followed by while loops validation
            new_user = input(f"Please Enter New User Name: ")
            # While loop if the new username already exists, notifying the user accordingly.
            while new_user in login_user:
                print(f"{RED}Username \'{new_user}\' Has Already Been Taken.{WHITE}")
                new_user = input(f"Please Enter A New User Name: ")
            # While loop if the new username is new, requesting the combination of new username and new password.
            while new_user not in login_user:
                # Additional function to return to main menu is '0' is entered.
                if new_user == "0":
                    print(f"{ITALIC_S}{GREEN}=> Returning to Main Menu <={ITALIC_E}{WHITE}")
                    user_file.close()
                    break
                # Otherwise append new username to the list
                login_user.append(new_user)
                # Request input of a new password for the new user.
                new_pass = input(f"Please Enter A Password For The New User: ")
                # Additional function to return to main menu is '0' is entered
                if new_pass == "0":
                    print(f"{ITALIC_S}{GREEN}=>Returning to Main Menu.<={ITALIC_E}{WHITE}")
                    user_file.close()
                    break
                # Request input of password confirmation.
                confirm_pass = input(f"Please Confirm The Password entered: ")
                # Confirm password against password to check if the new password and confirmed password are the same.
                # While loop validating if new password differs from the originally entered and advise user accordingly.
                while new_pass != confirm_pass:
                    print(f"{RED}Passwords are different. Please try again.{WHITE}")
                    new_pass = input(f"Please Enter A Password For The New User: ")
                    confirm_pass = input(f"Please Confirm The Password Entered: ")
                # When the passwords match, writes new user details to the file 'user.txt'
                if new_pass == confirm_pass:
                    user_file.write(f"\n{new_user}, {new_pass}")
                    user_file.close()
                    print(f"{GREEN}New Username And Password Have Been Successfully Added.{WHITE}")
        # If user is not 'admin' advise user accordingly, printing an error message
        else:
            print(f"───────────────────────────────────────────────────────\n"
                  f"{RED}You Need Administrative Rights To Login New Users.{WHITE}")

    # ====Add Task Section====
    # If the user enters 'a', they will be able to add a new task.
    # They will be asked to provide the necessary details and the task will be printed to a text file 'tasks.txt'.
    elif menu_option == "a":
        print(f"───────────────────────────────────────────────────────\n\t\t\t\t\t ADD TASK\n"
              f"───────────────────────────────────────────────────────")
        # === Add task user assignment ===
        # Open the 'user.txt' file where users are enrolled on reading mode only for user validation.
        user_file = open("user.txt", "r", encoding='utf-8-sig')
        # request the user details
        assigned_user = input(f"Who Is This Task Assigned To? Please Enter The Username\n==> ")
        # Additional function to return to main menu is '0' is entered.
        if assigned_user == "0":
            print(f"{ITALIC_S}{GREEN}=> Returning to Main Menu <={ITALIC_E}{WHITE}")
            user_file.close()
            continue
        # Validation through while loop and checking that user is in 'user.txt' and notify user accordingly.
        while assigned_user not in login_user:
            assigned_user = input(f"{RED}Username \'{assigned_user}\' Not Recognised.{WHITE} Please Try Again:\n==> ")
        # Close the 'user.txt' file as it is no loger required.
        user_file.close()

        # === Add task title === Prompting the user for task title.
        task_title = input(f"Please Enter The Title Of The Task:\n==> ")
        # Additional function to return to main menu is '0' is entered.
        if task_title == "0":
            print(f"{ITALIC_S}{GREEN}=> Returning to Main Menu <={ITALIC_E}{WHITE}")
            user_file.close()
            continue

        # === Add task description === Prompting the user for task description.
        task_description = input(f"Please Enter The description Of The Task:\n==> ")
        # Additional function to return to main menu is '0' is entered.
        if task_description == "0":
            print(f"{ITALIC_S}{GREEN}=> Returning to Main Menu <={ITALIC_E}{WHITE}")
            user_file.close()
            continue

        # === Add Task due date === Prompting the user for task due date.
        task_due_date = input(f"Please Enter The Due Date For The Task (DD/MM/YY):\n==> ").split("/")
        # Additional function to return to main menu is '0' is entered.
        if task_due_date == ["0"]:
            print(f"{ITALIC_S}{GREEN}=> Returning to Main Menu <={ITALIC_E}{WHITE}")
            user_file.close()
            continue
        # Additional function to validate the correct date format entered.
        # Originally maintaining to one format 'dd/mm/yy'.
        day, month, year = task_due_date[0], task_due_date[1], task_due_date[2]
        while True:
            if len(day) > 2 or len(month) > 2 or len(year) != 2:
                task_due_date = input(f"{RED}Wrong Format date.{WHITE}\n"
                                      f"Please Enter The Due Date For The Task (DD/MM/YY):\n==> ").split("/")
                day, month, year = task_due_date[0], task_due_date[1], task_due_date[2]
            else:
                break
        # Finally converting onto the format to be stored on file 'dd mmm yyyy'.
        task_due_date = datetime(2000 + int(year), int(month), int(day)).strftime("%d %b %Y")

        # === Add Task Status ===
        # Prompting the user for task status, validating the first character entered by the user as 'y or n',
        # Otherwise inform the user accordingly.
        while True:
            task_status = input("Has the task been concluded (Y/N)?\n==> ")
            if task_status == "" or not task_status[0].lower() in ["y", "n"]:
                print(f"{RED}Wrong Format. Please answer yes or no!{WHITE}")
            else:
                break
        if task_status[0].lower() == 'y':
            task_status = "Yes"
        if task_status[0].lower() == 'n':
            task_status = "No"
        # Open the 'tasks.txt' file on appending mode to append the above information.
        tasks_file = open("tasks.txt", "a+", encoding='utf-8-sig')
        tasks_file.write(f"\n{assigned_user}, {task_title}, {task_description}, {todays_date}, {task_due_date}, "
                         f"{task_status}")
        # close the 'tasks.txt' file once information is stored and advise the user accordingly.
        tasks_file.close()
        print(f"{GREEN}New Task Has Been Added Successfully On {todays_date}.{WHITE}")

    # ====View All Tasks Section====
    # If the user enters 'va', the details of all tasks for all registered users will be shown and the user advised.
    elif menu_option == "va":
        print(f"───────────────────────────────────────────────────────\n\t\t\t\t\tVIEW ALL TASKS")
        # Open the 'tasks.txt' file on reading mode to read the lines of the file for the relevant information.
        tasks_file = open("tasks.txt", "r", encoding='utf-8-sig')
        tasks_details = tasks_file.readlines()
        # To assess the amount of tasks in total
        total_tasks = len(tasks_details)
        # for loop through each line of the file, enumerating each task and output the information accordingly.
        for pos, line in enumerate(tasks_details, 1):
            # Split that line where there is comma and space.
            tasks_details = line.rstrip('\n').split(", ")
            # Then print the results in the format shown in the Output 2
            print(f"───────────────────────────────────────────────────────\n"
                  f"Task {pos} :\t\t\t\t{tasks_details[1]}\n"
                  f"Assigned To:\t\t\t{tasks_details[0]}\n"
                  f"Date Assigned:\t\t\t{tasks_details[3]}\n"
                  f"Due Date:\t\t\t\t{tasks_details[4]}\n"
                  f"Task Complete?:\t\t\t{tasks_details[5]}\n"
                  f"Task description:\n{tasks_details[2]}")
        # Prompt the user accordingly and close the 'tasks.txt' file as no loger required.
        print(f"───────────────────────────────────────────────────────\n"
              f"{GREEN}All {total_tasks} Have Been Listed Above ({todays_date}).{WHITE}")
        tasks_file.close()

    # ====View My Tasks Section====
    # If the user enters 'vm', the details of all tasks associated with the user will be shown and the user advised.
    elif menu_option == "vm":
        print(f"───────────────────────────────────────────────────────\n\t\t\t\t\tVIEW MY TASKS")
        # Open the 'tasks.txt' file on reading mode to read the lines of the file for the relevant information.
        tasks_file = open("tasks.txt", "r", encoding='utf-8-sig')
        tasks_details = tasks_file.readlines()
        # Counter for the tasks associated with the user.
        total_tasks = 1
        # for loop through each line of the file, enumerating each task and output the information accordingly.
        for pos, line in enumerate(tasks_details, 1):
            # Split the line where there is comma and space
            tasks_details = line.rstrip('\n').split(", ")
            # Check if the username of the person logged in is the same as the username you have read from the file.
            my_task = tasks_details[0]
            # Validate all tasks associated with the user and print them accordingly.
            if my_task == user_name:
                # If they are the same print it in the format of Output 2 in the task PDF
                print(f"───────────────────────────────────────────────────────\n"
                      f"Task {pos} :\t\t\t\t{tasks_details[1]}\n"
                      f"Assigned To:\t\t\t{tasks_details[0]}\n"
                      f"Date Assigned:\t\t\t{tasks_details[3]}\n"
                      f"Due Date:\t\t\t\t{tasks_details[4]}\n"
                      f"Task Complete?:\t\t\t{tasks_details[5]}\n"
                      f"Task description:\n{tasks_details[2]}")
                total_tasks += 1
        # Prompt the user accordingly and close the 'tasks.txt' file as no loger required.
        print(f"───────────────────────────────────────────────────────\n"
              f"{GREEN}All {total_tasks - 1} Tasks Assigned To \'{user_name}\' "
              f"Have Been Listed Above ({todays_date}).{WHITE}")
        tasks_file.close()

    # ====View Statistics Section====
    # If the user inputs 's' and the user is the 'admin', the total number of tasks and
    # the total number of users are displayed.
    elif menu_option == "s":
        print(f"───────────────────────────────────────────────────────\n\t\t\t\tOVERALL STATISTICS\n"
              f"───────────────────────────────────────────────────────")
        # Open the 'tasks.txt' file on reading mode to read the lines of the file for the relevant information.
        # Inform the user about the total number of tasks that have been logged and close the associated file afterwards
        tasks_file = open("tasks.txt", "r", encoding='utf-8-sig')
        for line in tasks_file:
            tasks_total = tasks_file.readlines()
            print(f"Total Of Registered Tasks:", len(tasks_total)+1)
        tasks_file.close()
        # Open the 'user.txt' file on reading mode to read the lines of the file for the relevant information.
        # Inform the user about the total number of users that have been logged and close the associated file afterwards
        user_file = open("user.txt", "r", encoding='utf-8-sig')
        for line in user_file:
            users_total = user_file.readlines()
            print(f"Total Of Registered Users:", len(users_total)+1)
        user_file.close()
        print(f"{GREEN}These Are The Statics At Today's Date: {todays_date}.{WHITE}")
    # ====Exit Section====
    # If the user inputs 'e' the main if-elif-else statement is stopped and the program exits.
    elif menu_option == "e":
        print(f"{GREEN}Thank You \'{user_name}\'. Goodbye !!!{WHITE}")
        break
    # If the user has entered an option not recognised, the user is notified accordingly.
    else:
        print(f"{RED}You Have Made A Wrong Choice, Please Try Again.{WHITE}")
