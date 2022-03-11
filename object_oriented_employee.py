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

    def read_first_name(self):
        while True:
            self.firstname = input(f"Please Enter The First Name: ")
            if len(self.firstname.strip()) > 1:
                return self.firstname
            else:
                print("Name must be a minimum of 2 characters")

    def print_first_name(self):
        print(self.firstname.capitalize().strip())

    def read_last_name(self):
        while True:
            self.lastname = input(f"Please Enter The Last Name: ")
            if len(self.lastname.strip()) > 1:
                return self.lastname
            else:
                print("Name must be a minimum of 2 characters")

    def print_last_name(self):
        print(self.lastname.capitalize().strip())

    def read_birth_day(self):
        while True:
            self.birthday = input("Please Enter Employee Birth Day: ")
            self.birthday = self.birthday.strip()
            if self.birthday.strip():
                self.birthday = int(self.birthday)
                if (self.birthday >= 1) and (self.birthday <= 31):
                    return self.birthday
                else:
                    print("Employee Birth Day must be between 1 and 31")
            else:
                print("Employee Birth Day must contain only digits")

    def print_birth_day(self):
        print(self.birthday)


    def read_birth_month(self):
        while True:
            self.birthmonth = input("Please Enter Employee Birth Month: ")
            self.birthmonth = self.birthmonth.strip()
            if self.birthmonth.isdigit():
                self.birthmonth = int(self.birthmonth)
                if (self.birthmonth >= 1) and (self.birthmonth <= 12):
                    return self.birthmonth
                else:
                    print("Employee Birth Month must be between 1 and 12")
            else:
                print("Employee Birth Month must contain only digits")

    def print_birth_month(self):
        print(self.birthmonth)

    def read_birth_year(self):
        while True:
            self.birthyear = input("Please Enter Employee Birth Year: ")
            self.birthyear = self.birthyear.strip()
            if self.birthyear.isdigit():
                self.birthyear = int(self.birthyear)
                if (self.birthyear >= 1900) and (self.birthyear <= 2004):
                    return self.birthyear
                else:
                    print("Employee Birth Year must be between 1900 and 2004")
            else:
                print("Employee Birth Year must contain only digits")

    def print_birth_year(self):
        print(self.birthyear)

    def read_position(self):
        while True:
            self.position = input("Please Enter The Employee Position:")
            if len(self.position.strip()) > 0:
                self.position = str(self.position)
                return self.position
            else:
                print("WARNING: Enter Valid Employee Position")

    def print_position(self):
        print(self.position)

    def read_graduate(self):
        valid_choices = ["Y", "y", "N", "n"]
        while True:
            self.graduate = input("Has the Employee Graduated? Type 'y' for Yes or 'n' for No: ")
            if self.graduate in valid_choices:
                if self.graduate.lower() == "y":
                    return True
                return False
            else:
                print("Please Type 'y' or 'n'")

    def print_graduate(self):
        print(self.graduate)

    def read_id(self):
        while True:
            self.id = input("Please Enter Employee ID: ")
            self.id = self.id.strip()
            if (self.id.isdigit()) > 0:
                self.id = int(self.id)
                return self.id
            else:
                print("Enter valid Employee ID:")

    def print_id(self):
        print(self.id)


if __name__ == "__main__":

    employee1 = Employee()

    employee1.read_first_name()
    employee1.print_first_name()
    employee1.read_last_name()
    employee1.print_last_name()
    employee1.read_birth_day()
    employee1.print_birth_day()
    employee1.read_birth_month()
    employee1.print_birth_month()
    employee1.read_birth_year()
    employee1.print_birth_year()
    employee1.read_position()
    employee1.print_position()
    employee1.read_graduate()
    employee1.print_graduate()
    employee1.read_id()
    employee1.print_id()

    print(employee1)