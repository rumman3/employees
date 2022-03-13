class Employee:

    employees = {}                   ##put dictionary inside class, so it's easier to access all the details.
                                     ##if it was outside, you can't access without 'returns'

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.birthday = None
        self.birthmonth = None
        self.birthyear = None
        self.position = ""
        self.graduate = None
        self.id = None

    def read_id(self):
        while True:
            self.id = input("Please Enter Employee ID: ")
            self.id = self.id.strip()
            if (self.id.isdigit() > 0) and (self.id not in Employee.employees.keys()):
                self.id = int(self.id)
                break
            else:
                print("Enter another valid Employee ID:")

    def read_first_name(self):
        while True:
            self.firstname = input(f"Please Enter The First Name: ")
            if len(self.firstname.strip()) > 1:
                break
            else:
                print("Name must be a minimum of 2 characters")

    def read_last_name(self):
        while True:
            self.lastname = input(f"Please Enter The Last Name: ")
            if len(self.lastname.strip()) > 1:
                break
            else:
                print("Name must be a minimum of 2 characters")

    def read_birth_day(self):
        while True:
            self.birthday = input("Please Enter Employee Birth Day: ")
            self.birthday = self.birthday.strip()
            if self.birthday.strip():
                self.birthday = int(self.birthday)
                if (self.birthday >= 1) and (self.birthday <= 31):
                    break
                else:
                    print("Employee Birth Day must be between 1 and 31")
            else:
                print("Employee Birth Day must contain only digits")

    def read_birth_month(self):
        while True:
            self.birthmonth = input("Please Enter Employee Birth Month: ")
            self.birthmonth = self.birthmonth.strip()
            if self.birthmonth.isdigit():
                self.birthmonth = int(self.birthmonth)
                if (self.birthmonth >= 1) and (self.birthmonth <= 12):
                    break
                else:
                    print("Employee Birth Month must be between 1 and 12")
            else:
                print("Employee Birth Month must contain only digits")

    def read_birth_year(self):
        while True:
            self.birthyear = input("Please Enter Employee Birth Year: ")
            self.birthyear = self.birthyear.strip()
            if self.birthyear.isdigit():
                self.birthyear = int(self.birthyear)
                if (self.birthyear >= 1900) and (self.birthyear <= 2004):
                    break
                else:
                    print("Employee Birth Year must be between 1900 and 2004")
            else:
                print("Employee Birth Year must contain only digits")

    def read_position(self):
        while True:
            self.position = input("Please Enter The Employee Position:")
            if len(self.position.strip()) > 0:
                self.position = str(self.position)
                break
            else:
                print("WARNING: Enter Valid Employee Position")

    def read_graduate(self):
        valid_choices = ["Y", "y", "N", "n"]
        while True:
            self.graduate = input("Has the Employee Graduated? Type 'y' for Yes or 'n' for No: ")
            if self.graduate in valid_choices:
                if self.graduate.lower() == "y":
                    self.graduate = True
                self.graduate = False
                break
            else:
                print("Please Type 'y' or 'n'")


    def print_all_data(self):
        print(f"Employee ID: {self.id}")
        print(f"Employee First Name: {self.firstname.capitalize().strip()}")
        print(f"Employee Last Name: {self.lastname.capitalize().strip()}")
        print(f"Employee Birth Date: {self.birthday}/{self.birthmonth}/{self.birthyear}")
        print(f"Employee Position: {self.position.capitalize().strip()}")
        print(f"Employee is a Graduate: {self.graduate}")

    def add_employee(self):
        self.read_id()
        self.read_first_name()
        self.read_last_name()
        self.read_birth_day()
        self.read_birth_month()
        self.read_birth_year()
        self.read_position()
        self.read_graduate()

    @staticmethod       ##Static when you make a method that isn't involving the class (i.e. not going to use Self)
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

    @staticmethod
    def remove_employee():
        while True:
            removeid_str = input("Please Enter the Employee ID that you want to remove: ")
            if removeid_str.isdigit():
                removeid = int(removeid_str)
                return removeid
            else:
                print("Enter valid Employee ID: ")

    @staticmethod
    def retrieve_details():
        while True:
            retreiveid_str = input("Please Enter the ID of the Employee's details you wish to Retrieve: ")
            if retreiveid_str.isdigit():
                retrieveid = int(retreiveid_str)
                return retrieveid
            else:
                print("Enter valid Employee ID: ")

    @staticmethod
    def update_details():
        while True:
            update_details_str = input("Please Enter the ID of the Employee's details you wish to update: ")
            if update_details_str.isdigit():
                update_details = int(update_details_str)
                return update_details


if __name__ == "__main__":


    while True:
        options = Employee.read_options()     ##access the 'read_options' static method

        if options.lower() == "a":
            employee = Employee()
            employee.add_employee()
            Employee.employees[employee.id] = employee ##Employee. is to access the class    ##.employees is to access dictionary
                                                       ##employee.id is to be able to access details via id
                                                       ##=employee is the variable that stores this particular employee's details
            employee.print_all_data()

        elif options.lower() == "r":
            remove_id = Employee.remove_employee()
            del Employee.employees[remove_id]
            print(f"Employee with id {remove_id} is removed")
            print(Employee.employees)

        elif options.lower() == "t":
            total_employees = len(Employee.employees.keys()) ##returns a 'list' of all the keys (IDs) & len counts the no. of keys of dictionary
            print(f"The Total No. of Employees in the system are {total_employees}")

        elif options.lower() == "l":
            list_of_employees = list(Employee.employees.values()) ##values are all the employees' details
            for employee in list_of_employees:
                employee.print_all_data()

        elif options.lower() == "ret":
            retrieveID = Employee.retrieve_details()
            Employee.employees[retrieveID].print_all_data()

        elif options.lower() == "u":
            change_details = Employee.update_details()   ##variable to access ID
            employee = Employee.employees[change_details]
            valid_inputs = ["firstname", "lastname", "birthday", "birthmonth", "birthyear", "position", "graduate"]
            while True:
                update = input("What details would you like to update? Choose from following: "
                           "\nfirstname \nlastname \nbirthday \nbirthmonth \nbirthyear \nposition \ngraduate ")
                if update in valid_inputs:
                    break
                else:
                    print("Please type the detail exactly as shown: ")
            mod = input("What would you like to modify this detail to? ")

            if update == "firstname":
                employee.first_name = mod
            elif update == "lastname":
                employee.last_name = mod
            elif update == "birthday":
                employee.birth_day = mod
            elif update == "birthmonth":
                employee.read_birth_month = mod
            elif update == "birthyear":
                employee.read_birth_year = mod
            elif update == "position":
                employee.read_position = mod
            elif update == "graduate":
                employee.read_graduate = mod
            employee.print_all_data()

        else:
            break
