import json
import os
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

DATA_FILE = "employees.json"

# === Email Sender Class ===
class EmailSender:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, employee_name, employee_email, email_subject, email_body):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = employee_email
        message["Subject"] = email_subject

        message.attach(MIMEText(email_body, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, employee_email, message.as_string())
                print(f"📧 Confirmation email sent to {employee_email}")
        except Exception as e:
            print("❌ Email not sent.")
            print(e)

# === Employee Class ===
class Employee:
    def __init__(self, id, name, department, salary, email):
        self.id = id
        self.name = name
        self.department = department
        self.salary = float(salary)
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "email": self.email
        }

    def display(self):
        print("\n--- Employee Details ---")
        print(f"ID        : {self.id}")
        print(f"Name      : {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary    : ${self.salary:.2f}")
        print(f"Email     : {self.email}")
        print("------------------------")

# === Manager Class ===
class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.load_data()
        self.email_sender = EmailSender("pradhushaasa@gmail.com", "cvqk wagd eeyo gmhe")  # Replace with real email/app password

    def is_unique_id(self, id):
        return all(emp.id != id for emp in self.employees)

    def is_valid_id(self, id):
        return re.fullmatch(r'S\d{7}', id) is not None

    def is_valid_name(self, name):
        return name.replace(" ", "").isalpha()

    def is_valid_salary(self, salary_str):
        try:
            return float(salary_str) >= 0
        except ValueError:
            return False

    def is_valid_email(self, email):
        return re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", email) is not None

    def add_employee(self):
        print("\n--- Add Employee ---")
        while True:
            id = input("Enter ID (e.g., S1234567): ").strip()
            if not self.is_valid_id(id):
                print("⚠ ID must start with 'S' followed by exactly 7 digits.")
            elif not self.is_unique_id(id):
                print("⚠ ID already exists.")
            else:
                break

        while True:
            name = input("Enter Name: ").strip()
            if self.is_valid_name(name):
                break
            print("⚠ Invalid name. Letters and spaces only.")

        department = input("Enter Department: ").strip()
        if not department:
            print("⚠ Department cannot be empty.")
            return

        while True:
            salary_str = input("Enter Salary: ").strip()
            if self.is_valid_salary(salary_str):
                salary = float(salary_str)
                break
            print("⚠ Invalid salary.")

        while True:
            email = input("Enter Email: ").strip()
            if self.is_valid_email(email):
                break
            print("⚠ Invalid email format.")

        emp = Employee(id, name, department, salary, email)
        self.employees.append(emp)
        print("✅ Employee added.")

        subject = "Welcome to BitFutura!"
        body = f"""
Hello {name},

Welcome to the {department} department at BitFutura!
We are excited to have you on board. Your employee ID is {id}, and your registered salary is ${salary:.2f}.

Regards,  
HR Team  
BitFutura
"""
        self.email_sender.send_email(name, email, subject, body)

    def view_employee(self):
        id = input("Enter ID to view: ").strip()
        for emp in self.employees:
            if emp.id == id:
                emp.display()
                return
        print("❌ Employee not found.")

    def update_employee(self):
        id = input("Enter ID to update: ").strip()
        for emp in self.employees:
            if emp.id == id:
                print("Leave blank to keep current value.")

                name = input(f"New Name [{emp.name}]: ").strip()
                if name and self.is_valid_name(name):
                    emp.name = name

                dept = input(f"New Department [{emp.department}]: ").strip()
                if dept:
                    emp.department = dept

                salary_str = input(f"New Salary [{emp.salary}]: ").strip()
                if salary_str and self.is_valid_salary(salary_str):
                    emp.salary = float(salary_str)

                email = input(f"New Email [{emp.email}]: ").strip()
                if email and self.is_valid_email(email):
                    emp.email = email

                print("✅ Employee updated.")
                return
        print("❌ Employee not found.")

    def delete_employee(self):
        id = input("Enter ID to delete: ").strip()
        for emp in self.employees:
            if emp.id == id:
                confirm = input(f"Confirm delete {emp.name}? (y/n): ").lower()
                if confirm == 'y':
                    self.employees.remove(emp)
                    print("✅ Deleted.")
                else:
                    print("❌ Cancelled.")
                return
        print("❌ Employee not found.")

    def list_all_employees(self):
        if not self.employees:
            print("📂 No employee records.")
            return
        for emp in self.employees:
            emp.display()

    def department_wise_report(self):
        if not self.employees:
            print("📂 No employee records.")
            return

        report = {}
        for emp in self.employees:
            report.setdefault(emp.department, []).append(emp)

        print("\n📊 Department-Wise Report")
        for dept, emps in report.items():
            print(f"\nDepartment: {dept} ({len(emps)} employees)")
            for emp in emps:
                print(f" - {emp.name} (ID: {emp.id}, Salary: ${emp.salary:.2f})")

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump([e.to_dict() for e in self.employees], f, indent=4)
        print("💾 Data saved.")

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    for d in json.load(f):
                        self.employees.append(Employee(**d))
                print("📂 Data loaded.")
            except Exception as e:
                print(f"⚠ Error loading data: {e}")
        else:
            print("📁 No data file found.")

    def menu(self):
        while True:
            print("\n📁 Employee Management System")
            print("1. Add Employee")
            print("2. View Employee")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. List All Employees")
            print("6. Department Wise Report")
            print("7. Exit")

            choice = input("Enter choice (1-7): ").strip()
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_employee()
            elif choice == '3':
                self.update_employee()
            elif choice == '4':
                self.delete_employee()
            elif choice == '5':
                self.list_all_employees()
            elif choice == '6':
                self.department_wise_report()
            elif choice == '7':
                self.save_data()
                print("👋 Goodbye.")
                break
            else:
                print("❌ Invalid choice. Try again.")

# === Run the system ===
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
