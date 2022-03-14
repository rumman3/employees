class Employee:

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.birthday = None
        self.birthmonth = None
        self.birthyear = None
        self.position = ""
        self.graduate = None
        self.id = None

    def read_id(self, employees):
        while True:
            try:
                self.id = int(input("Please Enter Employee ID: "))
            except ValueError:
                print("The ID should only contain digits")
                continue   ##continue brings you back to the top of the loop to try again
            if self.id not in employees.keys():
                return self.id
            else:
                print("This ID is already taken")


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

    def __str__(self):
        text = f"Employee ID: {self.id} \nEmployee First Name: {self.firstname.capitalize().strip()} " \
               f"\nEmployee Last Name: {self.lastname.capitalize().strip()}\nEmployee Birth Date: {self.birthday}/" \
               f"{self.birthmonth}/{self.birthyear} \nEmployee Position: {self.position.capitalize().strip()}" \
               f"\nEmployee is a Graduate: {self.graduate}"

        return text

    def add_employee(self, employees):
        self.read_id(employees)
        self.read_first_name()
        self.read_last_name()
        self.read_birth_day()
        self.read_birth_month()
        self.read_birth_year()
        self.read_position()
        self.read_graduate()


    ##Static when you make a method that isn't involving the class (i.e. not going to use Self)
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

def read_options(): ##outside of class (not needed in class)
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

if __name__ == "__main__":

    employees = {}

    while True:
        options = read_options()     ##access the 'read_options' static method

        if options.lower() == "a":
            employee = Employee()
            employee.add_employee(employees)
            employees[employee.id] = employee ##Employee. is to access the class    ##.employees is to access dictionary
                                                       ##employee.id is to be able to access details via id
                                                       ##=employee is the variable that stores this particular employee's details
            print(str(employee))          ## str returns all the __str__ data & print() prints it

        elif options.lower() == "r":
            while True:
                remove_id = Employee.remove_employee()
                try:
                    del employees[remove_id]
                    break
                except KeyError:               ## KeyError is trying to look for a key in a dictionary that does not exist
                    print("This id does not exist")

            print(f"Employee with id {remove_id} is removed")


        elif options.lower() == "t":
            total_employees = len(employees.keys()) ##returns a 'list' of all the keys (IDs) & len counts the no. of keys of dictionary
            print(f"The Total No. of Employees in the system are {total_employees}")

        elif options.lower() == "l":
            list_of_employees = list(employees.values()) ##values are all the employees' details
            for employee in list_of_employees:
                print(str(employee))

        elif options.lower() == "ret":
            while True:
                retrieveID = Employee.retrieve_details()
                try:
                    print(str(employees[retrieveID]))
                    break
                except KeyError:
                    print("This id does not exist")


        elif options.lower() == "u":
            change_details = Employee.update_details()   ##variable to access ID
            employee = employees[change_details]
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
            print(str(employee))

        else:
            break
