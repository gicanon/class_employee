from datetime import datetime

class User:
    
    def __init__(self, id, name, password, role):
        """Initializes a User object.
        id: int
        name: string
        password: string
        role: string
        """
        self.userID = id
        self.userName = name
        self.password = password
        self.UserRole = role

    def login(self):
        pass
    
    def update(self):
        pass

class Employee(User):

    def __init__(self, id, name, department, phone, quali):
        """Initializes a Employee object.
        id: int
        name: string
        dpartment: string
        phone: string
        quali: string"""

        self.userID = id
        self.userName = name
        self.department = department
        self.phoneNr = phone
        self.qualification = quali
        

    def applyLeave(self):
        """Booking annual leave day. Return the leave day"""

        leave_day = input('Enter the day of annual leave in mm/dd/yyyy format: ')
        leave_day = datetime.strptime(leave_day, '%m/%d/%Y')
        print(self.userName, end='')
        leave_day = leave_day.strftime('%A, %m/%d/%Y')
        print(", you just booked your annual leave day for", leave_day, 'please wait of the confirmation from your Manager')
        return leave_day

    def forControlManager(self, leave_day):
        """Printing name and leave day for Manager"""

        print(self.userName, 'has booked an annual leave day for', leave_day)

    def checkLeaveStatus(self, leave_day):
        """Printing status of the annual leave day request"""

        print(leave_day)

    def viewPayslip(self):
        pass
    
class Manager(Employee):

    def __init__(self, id, name, department, phone, quali):
        super().__init__(id, name, department, phone, quali)

    def viewReports():
        pass

    def viewEmployee(self):
        pass

    def editEmployee():
        pass

    def controlLeaveStatus(self, leave_day):
        """Confirmation or Rejecting from Manger of the annual leave day request from employee.
        Return Confirmation or Rejection"""

        input_info = input("""Please confirm or reject the booking and enter the proper number

1. Cofirming
2. Rejecting
""")
        if input_info == '1':
            return f'The annual leave day on {leave_day} is confirmed'
    
        elif input_info == '2':
            return f'The annual leave day on {leave_day} is rejected'
            
        else:
            print('Wrong input, please try again')
            return self.controlLeaveStatus(leave_day)


class Administrator(User):
    
    def addEmployee():
        pass
    
    def viewEmployee():
        pass

    def editEmployee():
        pass

    def editRole():
        pass

    def createNewUserLogin():
        pass

def main():
    """Executing of booking an annual leave day"""
    
    u1 = User(1, 'Max Mustermann', 'm12345678', 'Employee')
    u2 = User (2, 'Robert Heinrich', 'r87654321', 'Manager')
    e1 = Employee(u1.userID, u1.userName, 'Computer Science', '+4917683998870', 'Computer Scientist' )
    m1 = Manager(u2.userID, u2.userName, 'Computer Science', '+4179098867586', 'Project Manager')

    #Employee environment (booking annual leave day)
    print('Employee environment\n')
    leave_day = e1.applyLeave()

    #Manager environment (response to the employee's request to book a day of leave)
    print('\nManager environment\n')
    e1.forControlManager(leave_day)
    status = m1.controlLeaveStatus(leave_day)

    #Employee environment (checking response from Manager)
    print('\nEmployee environment\n')
    e1.checkLeaveStatus(status)

if __name__ == '__main__':
    main()


