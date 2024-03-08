
#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"



#=====defining functions===========

# Define function to register a new user.
def reg_user():

    # - Request input of a new username
    while True:
        new_username = input("New Username: ")

        if new_username in username_password:
            print("User already exists. Please insert another username.")
            new_username = input("New Username: ")
        else:
            break

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
        return 
        # return to main menu

    # - Otherwise present a relevant message.
    else:
        print("Passwords do no match")
    return

    



# define function to add a task.
# Allow a user to add a new task to task.txt file
# Prompt a user for the following:
#- A username of the person whom the task is assigned to,
#- A title of a task,
#- A description of the task and
#- the due date of the task.

def add_task():
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        else:
            break
     # If user does not exist, return to beginning of function.
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    # Add the new task to the task list variable.
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")
    return # return to main menu





# Function that reads the task from task.txt file and prints to the console
def view_all():

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n{t['description']}\n"
        print(disp_str)
    return




# Function that reads the task from task.txt file and 
# prints only the current user's tasks to the console
# Then gives user the option to edit due date/mark a task complete
def view_mine():
    # Read tasks belonging to the current user
    user_tasks = [task for task in task_list if task['username'] == curr_user]

    count = 0
    for i, t in enumerate(user_tasks, start=1):
        count += 1
        disp_str = f"Task: {i} \t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        disp_str += "Completed:\t Yes" if t['completed'] else "Completed:\t No"
        disp_str += "\n-----------------------------------------------------------------------\n"
        print(disp_str)

    task_num = int(input("Please insert the task number you would like to edit or insert -1 to exit: "))
    if task_num == -1:
        return
    else:
        # Get the selected task based on user's input
        selected_task = user_tasks[task_num - 1]
        edit_option = int(input("Enter 1 to mark the task as complete. Enter 2 to edit the task: "))
        if edit_option == 1:
            selected_task['completed'] = True
        elif edit_option == 2:
            if selected_task['completed']:
                print("Task has already been completed and cannot be edited.")
                return
            else:
                # gives user the option to edit due date/mark a task complete
                edit_selection = int(input("""Enter 1 edit the username of the person assigned to the task.
Enter 2 to edit the due date. """))
                if edit_selection == 2:
                    new_date_string = input("Enter the new due date for task in the following format yyyy-mm-dd:")
                    new_date = datetime.strptime(new_date_string, DATETIME_STRING_FORMAT)
                    selected_task['due_date'] = new_date
                elif edit_selection == 1:
                    new_username = input("Please enter the new username you want the task assigned to: ")
                    selected_task['username'] = new_username

        # Update the task list in the file
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
            print("Successfully updated the selected task.")




# Function to generate 2 txt files comtaining information about the tasks and users.
def gen_report():

    # Open file 'task_overview'
    with open('task_overview', 'w+') as grtask_overview:
            total_tasks = len(task_list)
            completed_tasks = 0
            uncompleted_tasks = 0
            overdue_tasks = 0
            curr_date = datetime.today()

            for task in task_list:
                if task['completed'] == True:
                    completed_tasks += 1
                elif task['completed'] == False: 
                    uncompleted_tasks += 1
            for task in task_list:
                if task['completed'] == False and task['due_date'] < curr_date:
                    overdue_tasks += 1

            completed_percentage = round((completed_tasks / total_tasks) * 100, 1)
            uncompleted_percentage = (round(uncompleted_tasks / total_tasks) * 100, 1)
            overdue_percentage = round((overdue_tasks / total_tasks) * 100, 1)
            overview_text = []

            # Write the following to the file task_overview.txt
            grtask_overview.write(
                f"\n-----------------------------------------------------------------------"
                f"\nTotal number of tasks currently stored in this program:  {total_tasks}" 
                f"\nTotal number of completed tasks:  {completed_tasks}" 
                f"\nTotal number of uncompleted tasks:  {uncompleted_tasks}" 
                f"\nTotal number of overdue tasks:  {overdue_tasks}"
                f"\nPercentage of tasks that are incomplete:  {uncompleted_percentage}%"
                f"\nPercentage of tasks that are overdue:  {overdue_percentage}%"
                f"\n-----------------------------------------------------------------------")
            
    # Open the file user_overview.txt
    with open('user_overview.txt', 'w+') as gruser_overview:
        num_users = len(username_password)
        gruser_overview.write(
                f"\n-----------------------------------------------------------------------"
                f"\nTotal number of users in this program: {num_users}"
                f"\nTotal number of tasks currently stored in this program:  {total_tasks}"
                f"\n-----------------------------------------------------------------------")
        for each_user in username_password:
            each_user_tasks = 0
            each_user_completed = 0
            each_user_uncompleted = 0
            percentage_user_complete = 0
            percentage_user_imcomplete = 0

            for each in task_list:
                if each_user == each['username']:
                    each_user_tasks += 1
                    if each['completed'] == True:
                        each_user_completed += 1
                    else:
                        each_user_uncompleted +=1

            percentage_ofall_users = round((each_user_tasks / total_tasks) * 100, 1)
            percentage_user_complete = round((each_user_completed / each_user_tasks) * 100, 1)
            percentage_user_imcomplete = round((each_user_uncompleted / each_user_tasks) * 100, 1)

            gruser_overview.write(
                f"\n\n\n-----------------------------------------------------------------------"
                f"\nUser: {each_user}"
                f"\n-----------------------------------------------------------------------"
                f"\nTotal number of tasks assigned to {each_user}:  {each_user_tasks}"
                f"\nPercentage of all tasks that have been assigned to {each_user}:  {percentage_ofall_users}"
                f"\nPercentage of tasks completed by {each_user}:  {percentage_user_complete}"
                f"\nPercentage of tasks currently uncompleted by {each_user}:  {percentage_user_imcomplete}"
                "\n-----------------------------------------------------------------------")
        print('The files "task_overview.txt" and "user_overview.txt have been successfully generated.')
    return



# Function to display to the console the files that are generated in the gen_report function
def disp_statistics():

    with open('task_overview', 'r') as grtask_overview:
        for line in grtask_overview:
            print(line)
    with open('user_overview.txt', 'r') as gruser_overview:
        for line in gruser_overview:
            print(line)





# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)



#====Login Section====
'''This code reads usernames and password from the user.txt file to
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()
    
    # Directs the program to the write function for each letter the user selects
    # If user enters wrong choice, they get error message and are looped back to main menu
    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
        
    elif menu == 'vm':
        view_mine()
            
    elif menu == 'gr':
        gen_report()
        
    elif menu == 'ds' and curr_user == 'admin': # only the admin user can select this option
        
        gen_report()
        disp_statistics()
        
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")