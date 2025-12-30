
# 🧑‍💼 Employee Management System (Python)

## 📌 Introduction
This project is a **menu-driven Employee Management System** developed using **Python**.  
It demonstrates **Object-Oriented Programming (OOP)** concepts such as **class, object, inheritance, encapsulation, constructor, method overriding, getters, setters**, and **lists of objects**.

The application runs in the terminal and allows the user to manage **Employees, Managers, and Developers**.

---

## 🧠 Concepts Covered (Deep Explanation)

### 🔹 Class
A **class** is a blueprint used to create objects.
It defines **attributes (data)** and **methods (functions)**.

Example:
```python
class Employee:
    pass
```

Here, `Employee` is a class.

---

### 🔹 Object
An **object** is an instance of a class.
It represents real-world entities.

Example:
```python
obj_emp = Employee(1, "Rahul", 25, 30000)
```

`obj_emp` is an object of the `Employee` class.

---

### 🔹 Constructor (`__init__`)
A constructor is a special method that is automatically called when an object is created.

```python
def __init__(self, emp_id, name, age, salary):
    self.__emp_id = emp_id
    self.name = name
    self.age = age
    self.__salary = salary
```

✔ Initializes object data  
✔ `self` refers to the current object

---

### 🔹 Encapsulation (Data Hiding)
Encapsulation hides internal data using **private variables**.

```python
self.__emp_id
self.__salary
```

Private variables **cannot be accessed directly** outside the class.

✔ Improves security  
✔ Prevents accidental modification

---

### 🔹 Getter and Setter Methods
Used to **access and modify private variables** safely.

Getter:
```python
def get_emp_id(self):
    return self.__emp_id
```

Setter:
```python
def set_salary(self, salary):
    self.__salary = salary
```

---

### 🔹 Inheritance
Inheritance allows one class to acquire properties of another class.

```python
class Manager(Employee):
```
`Manager` inherits from `Employee`.

✔ Reduces code duplication  
✔ Improves reusability

---

### 🔹 super() Keyword
Used to call parent class methods or constructor.

```python
super().__init__(emp_id, name, age, salary)
```

---

### 🔹 Method Overriding
When a child class provides its own implementation of a parent class method.

```python
def show(self):
    super().show()
    print(f"Department : {self.department}")
```

---

## 📂 Class-wise Explanation

### 1️⃣ Employee Class
Stores common employee information.

**Attributes**
- emp_id (private)
- name
- age
- salary (private)

**Methods**
- `get_emp_id()`
- `set_emp_id()`
- `get_salary()`
- `set_salary()`
- `show()`

---

### 2️⃣ Manager Class
Inherits from Employee.

**Additional Attribute**
- department

**Overridden Method**
- `show()`

---

### 3️⃣ Developer Class
Inherits from Employee.

**Additional Attribute**
- programming language

---

## 📦 Object Storage Using Lists
Objects are stored in lists.

```python
employee = []
manager = []
developer = []
```

✔ Each list stores multiple objects  
✔ Acts like a small database

---

## 🔁 Menu Driven Program
The program runs continuously using:

```python
while True:
```
Until the user chooses **Exit**.

---

## 📋 Menu Options Explained

### Create Employee
Takes input from user and creates Employee object.

### Create Manager
Creates Manager object using inheritance.

### Create Developer
Creates Developer object.

### Show Details
Displays stored data using object methods.

### Salary Update
Updates salary using setter method.

---

## 💰 Salary Update Logic
```python
if e.get_emp_id() == eid:
    e.set_salary(new_salary)
```

✔ Uses encapsulation  
✔ Safe update of private variable

---

## ⚠️ Bug Notice
In Developer creation:
```python
obj_dev = Manager(...)
```
Should be:
```python
obj_dev = Developer(...)
```

---

## ✅ Advantages of This Project
- Beginner friendly
- Clear OOP structure
- Real-world example
- Easy to extend

---

## 🚀 Conclusion
This project is an excellent example to understand **Python OOP practically**.  
It shows how classes and objects work together to build real applications.

---

📌 **Author:** Ritika  
📌 **Language:** Python  
📌 **Type:** Console Application
