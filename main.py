from employeeDetails import * ## asterix imports everything from employee details

if __name__ == '__main__':

    employees = {} ##actual dictionary (outside of loop so new employee data gets stored, not overidden

    while True:
        options = read_options()

        if options.lower() == "a":
            employee = add_employee()
            employees[employee["id"]] = employee  ##to add and store new employee to dictionary via its key, this is syntax to make dictionary of dictionaries
            print([employee])

        elif options.lower() == "r":
            remove_id = remove_employee()
            del employees[remove_id]
            print(f"Employee with id {remove_id} is removed")
            print(employees)

        elif options.lower() == "t":
            total_employees = len(employees.keys()) ##returns a 'list' of all the keys (IDs) & len counts the no. of keys of dictionary
            print(f"The Total No. of Employees in the system are {total_employees}")

        elif options.lower() == "l":
            list_of_employees = list(employees.values()) ##values are all the employees' details
            for employee in list_of_employees:
                print("\n", employee)

        elif options.lower() == "ret":
            retrieveID = retrieve_details()
            print(employees[retrieveID])

        elif options.lower() == "u":
            change_details = update_details()
            valid_inputs = ["first_name", "last_name", "birth_day", "birth_month", "birth_year", "position", "graduate"]
            while True:
                update = input("What details would you like to update? Choose from following: "
                           "\nfirst_name \nlast_name \nbirth_day \nbirth_month \nbirth_year \nposition \ngraduate ")
                if update in valid_inputs:
                    break
                else:
                    print("Please type chosen detail exactly as shown:")
            mod = input("What would you like to modify this detail  to? ")
            employees[change_details][update] = mod
            print(employees[change_details])

        else:
            break