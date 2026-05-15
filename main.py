import csv
import os
from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

FILE_NAME = "employees.csv"


# Create CSV File
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Post", "Salary"])


# Add Employee
def add_employee():

    print(Fore.CYAN + "\n===== Add Employee =====\n")

    emp_id = input("Enter Employee ID: ")

    # Check duplicate employee ID
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == emp_id:
                print(Fore.RED + "\nEmployee ID already exists!\n")
                return

    name = input("Enter Employee Name: ")
    post = input("Enter Employee Post: ")
    salary = input("Enter Employee Salary: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([emp_id, name, post, salary])

    print(Fore.GREEN + "\nEmployee Added Successfully!\n")

# Display Employees
def display_employees():

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    if len(data) <= 1:
        print(Fore.RED + "\nNo Employee Records Found\n")
        return

    print(Fore.YELLOW + "\n========== Employee Records ==========\n")

    headers = data[0]
    rows = data[1:]

    print(tabulate(rows, headers=headers, tablefmt="grid"))

    print(Fore.CYAN + f"Total Employees: {len(rows)}")

    print()


# Search Employee
def search_employee():

    emp_id = input("Enter Employee ID to Search: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:

            if row[0] == emp_id:

                print(Fore.GREEN + "\nEmployee Found\n")

                table = [
                    ["ID", row[0]],
                    ["Name", row[1]],
                    ["Post", row[2]],
                    ["Salary", row[3]]
                ]

                print(tabulate(table, tablefmt="grid"))

                found = True
                break

    if not found:
        print(Fore.RED + "\nEmployee Not Found\n")


# Remove Employee
def remove_employee():

    emp_id = input("Enter Employee ID to Remove: ")

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row[0] != emp_id:
                rows.append(row)
            else:
                found = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if found:
        print(Fore.GREEN + "\nEmployee Removed Successfully\n")
    else:
        print(Fore.RED + "\nEmployee ID Not Found\n")


# Update Salary
def update_salary():

    emp_id = input("Enter Employee ID: ")
    new_salary = input("Enter New Salary: ")

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row[0] == emp_id:
                row[3] = new_salary
                found = True

            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if found:
        print(Fore.GREEN + "\nSalary Updated Successfully\n")
    else:
        print(Fore.RED + "\nEmployee ID Not Found\n")


# Main Menu
def menu():

    create_file()

    while True:

        print(Fore.BLUE + Style.BRIGHT + """
=================================================
          EMPLOYEE MANAGEMENT SYSTEM
=================================================

1. Add Employee
2. Display Employees
3. Search Employee
4. Remove Employee
5. Update Salary
6. Exit

=================================================
""")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            display_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            remove_employee()

        elif choice == "5":
            update_salary()

        elif choice == "6":
            print(Fore.CYAN + "\nThank You For Using The System\n")
            break

        else:
            print(Fore.RED + "\nInvalid Choice\n")


# Start Program
menu()