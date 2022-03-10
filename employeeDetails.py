def read_employeeID():
    while True:
        employeeid_str = input("Please Enter Employee ID: ")
        employeeid_str = employeeid_str.strip()
        if (employeeid_str.isdigit()) > 0:
            employeeid = int(employeeid_str)
            return employeeid
        else:
            print("Enter valid Employee ID:")


def read_name(name_type):
    while True:
        name = input(f"Please Enter The {name_type}: ")
        if len(name.strip()) > 1:
            return name
        else:
            print("Name must be a minimum of 2 characters")


def read_year():
    while True:
        year_str = input("Please Enter Employee Birth Year: ")
        year_str = year_str.strip()
        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Employee Birth Year must be between 1900 and 2004")
        else:
            print("Employee Birth Year must contain only digits")


def read_month():
    while True:
        month_str = input("Please Enter Employee Birth Month: ")
        month_str = month_str.strip()
        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Employee Birth Month must be between 1 and 12")
        else:
            print("Employee Birth Month must contain only digits")


def read_day():
    while True:
        day_str = input("Please Enter Employee Birth Day: ")
        day_str = day_str.strip()
        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Employee Birth Day must be between 1 and 31")
        else:
            print("Employee Birth Day must contain only digits")


def read_position():
    while True:
        position_str = input("Please Enter The Employee Position:")
        if len(position_str.strip()) > 0:
            position = str(position_str)
            return position
        else:
            print("WARNING: Enter Valid Employee Position")


def read_grad():
    valid_choices = ["Y", "y", "N", "n"]
    while True:
        grad_str = input("Has the Employee Graduated? Type 'y' for Yes or 'n' for No: ")
        if grad_str in valid_choices:
            if grad_str.lower() == "y":
                return True
            return False
        else:
            print("Please Type 'y' or 'n'")


def read_options():
    valid_options = ["a", "r", "t", "l", "ret", "u", "e"]
    while True:
        options_str = input("Please select an option: \n'a' to Add Employee \n'r' to Remove Employee"
                            "\n't' to Check Total No. of Employees \n'l' to see a list of the Employee(s)' details"
                            "\n'ret' to Retrieve an Employee's Data \n'u' to Update an Employee Data \n'e' to Exit: ")
        options_str = options_str.strip()
        if options_str in valid_options:
            return options_str
        else:
            print("Please Enter a Valid Option:  a | r | t | l | ret | u | e  ")


def add_employee():
    id = read_employeeID()

    first_name = read_name("First Name")

    last_name = read_name("Last Name")

    birth_year = read_year()

    birth_month = read_month()

    birth_day = read_day()

    employee_position = read_position()

    graduate = read_grad()

    employee = {"first_name": first_name,
                "last_name": last_name,
                "id": id,
                "birth_day": birth_day,
                "birth_month": birth_month,
                "birth_year": birth_year,
                "position": employee_position,
                "graduate": graduate,
                }
    return employee


def remove_employee():
    while True:
        removeid_str = input("Please Enter the Employee ID that you want to remove: ")
        if removeid_str.isdigit():
            removeid = int(removeid_str)
            return removeid
        else:
            print("Enter valid Employee ID: ")

def retrieve_details():
    while True:
        retreiveid_str = input("Please Enter the ID of the Employee's details you wish to Retrieve: ")
        if retreiveid_str.isdigit():
            retrieveid = int(retreiveid_str)
            return retrieveid
        else:
            print("Enter valid Employee ID: ")

def update_details():
    while True:
        update_details_str = input("Please Enter the ID of the Employee's details you wish to update: ")
        if update_details_str.isdigit():
            update_details = int(update_details_str)
            return update_details