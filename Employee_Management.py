class Employee:
    def __init__(self,emp_id,name,age,salary):
        self.__emp_id = emp_id
        self.name = name
        self.age = age
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self,emp_id):
        self.__emp_id = emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    
    def show(self):
        print(f"Id : {self.__emp_id}"),
        print(f"Name : {self.name}"), 
        print(f"Age : {self.age}"),  
        print(f"Salary : {self.__salary}")
        

class Manager(Employee):
    def __init__(self,emp_id,name,age,salary,department):
        super().__init__(emp_id,name,age,salary)
        self.department = department

    def show(self):
        super().show()
        print(f"Department : {self.department}")

class Developer(Employee):
    def __init__(self,emp_id,name,age,salary,pro_lan):
        super().__init__(emp_id,name,age,salary)
        self.pro_lan = pro_lan

    def show(self):
        super().show()
        print(f"Programming Language : {self.pro_lan}") 
        
    def __del__(self):
        pass

employee = []
manager = []
developer = []

while True:
    print("Employee Management System")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Details")
    print("5. Salary Upadate")
    print("6. Exit")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        eid = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        obj_emp = Employee(eid, name, age, salary) 
        employee.append(obj_emp)
        print("Employee created successfully")
    
    elif ch == 2:
        eid = int(input("Enter Manager ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")
        obj_man = Manager(eid, name, age, salary,department) 
        manager.append(obj_man)
        print("Manager created successfully")
    
    elif ch == 3:
        eid = int(input("Enter Developer ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        pro_lan = input("Enter pro_lan: ")
        obj_dev = Manager(eid, name, age, salary, pro_lan) 
        developer.append(obj_dev)
        print("Manager created successfully")


    elif ch == 4:
        while True:
            print("choose one to show details")
            print("1.Employee")
            print("2.Manager")
            print("3.Developer")
            print("4.Exit")

            ch = int(input("Enter your choice:"))

            if ch == 1:
                print("Employee Details")
                for e in employee:
                    e.show()
            if  ch == 2:
                print("Manager Details")
                for e in manager:
                    e.show()
            if ch == 3:
                print("Developer Details")
                for e in developer:
                    e.show()
            if ch == 4:
                break
    
    elif ch == 5:
        eid = int(input("Enter Employee ID to update salary: "))
        new_salary = float(input("Enter new salary: "))

        for e in employee:
            if e.get_emp_id() == eid:     
                e.set_salary(new_salary)   
                print("Salary updated successfully")
                break
                 
    elif ch == 6:
        break
    else:
        print("invalid choice")
