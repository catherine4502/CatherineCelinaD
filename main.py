import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Database class
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.create_tables()
    
    def create_tables(self):
        # Create employees table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age TEXT,
            doj TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            address TEXT
        )
        """)
        
        # Create departments table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS departments(
            id INTEGER PRIMARY KEY,
            name TEXT
        )
        """)
        
        # Create salaries table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS salaries(
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            amount REAL,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
        """)
        
        # Create projects table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS projects(
            id INTEGER PRIMARY KEY,
            name TEXT,
            employee_id INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
        """)
        
        self.con.commit()

    # Insert Function for Employees
    def insert_employee(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("INSERT INTO employees VALUES (NULL,?,?,?,?,?,?,?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()
    
    # Insert Function for Departments
    def insert_department(self, name):
        self.cur.execute("INSERT INTO departments VALUES (NULL,?)", (name,))
        self.con.commit()
    
    # Insert Function for Salaries
    def insert_salary(self, employee_id, amount):
        self.cur.execute("INSERT INTO salaries VALUES (NULL,?,?)", (employee_id, amount))
        self.con.commit()
    
    # Insert Function for Projects
    def insert_project(self, name, employee_id):
        self.cur.execute("INSERT INTO projects VALUES (NULL,?,?)", (name, employee_id))
        self.con.commit()

    # Fetch All Employees
    def fetch_employees(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows
    
    # Fetch All Departments
    def fetch_departments(self):
        self.cur.execute("SELECT * FROM departments")
        rows = self.cur.fetchall()
        return rows
    
    # Fetch All Salaries
    def fetch_salaries(self):
        self.cur.execute("SELECT * FROM salaries")
        rows = self.cur.fetchall()
        return rows
    
    # Fetch All Projects
    def fetch_projects(self):
        self.cur.execute("SELECT * FROM projects")
        rows = self.cur.fetchall()
        return rows

    # Delete an Employee
    def remove_employee(self, id):
        self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
        self.con.commit()
    
    # Delete a Department
    def remove_department(self, id):
        self.cur.execute("DELETE FROM departments WHERE id=?", (id,))
        self.con.commit()
    
    # Delete a Salary record
    def remove_salary(self, id):
        self.cur.execute("DELETE FROM salaries WHERE id=?", (id,))
        self.con.commit()
    
    # Delete a Project
    def remove_project(self, id):
        self.cur.execute("DELETE FROM projects WHERE id=?", (id,))
        self.con.commit()

    # Update an Employee
    def update_employee(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute(
            "UPDATE employees SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? WHERE id=?",
            (name, age, doj, email, gender, contact, address, id))
        self.con.commit()
    
    # Update a Department
    def update_department(self, id, name):
        self.cur.execute(
            "UPDATE departments SET name=? WHERE id=?", (name, id))
        self.con.commit()
    
    # Update a Salary record
    def update_salary(self, id, employee_id, amount):
        self.cur.execute(
            "UPDATE salaries SET employee_id=?, amount=? WHERE id=?", (employee_id, amount, id))
        self.con.commit()
    
    # Update a Project
    def update_project(self, id, name, employee_id):
        self.cur.execute(
            "UPDATE projects SET name=?, employee_id=? WHERE id=?", (name, employee_id, id))
        self.con.commit()

# Tkinter GUI
db = Database("employee_management.db")
root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()
department_name = StringVar()
salary_amount = StringVar()
project_name = StringVar()
project_employee_id = StringVar()

# Employees Frame
def employees_frame():
    employees_frame = Frame(root, bg="#535c68")
    employees_frame.pack(side=TOP, fill=X)
    
    lblName = Label(employees_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
    lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtName = Entry(employees_frame, textvariable=name, font=("Calibri", 16), width=30)
    txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    lblAge = Label(employees_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtAge = Entry(employees_frame, textvariable=age, font=("Calibri", 16), width=30)
    txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    lbldoj = Label(employees_frame, text="D.O.J", font=("Calibri", 16), bg="#535c68", fg="white")
    lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    txtDoj = Entry(employees_frame, textvariable=doj, font=("Calibri", 16), width=30)
    txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    lblEmail = Label(employees_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
    lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtEmail = Entry(employees_frame, textvariable=email, font=("Calibri", 16), width=30)
    txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    lblGender = Label(employees_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
    lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    comboGender = ttk.Combobox(employees_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
    comboGender['values'] = ("Male", "Female")
    comboGender.grid(row=3, column=1, padx=10, sticky="w")

    lblContact = Label(employees_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
    lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtContact = Entry(employees_frame, textvariable=contact, font=("Calibri", 16), width=30)
    txtContact.grid(row=3, column=3, padx=10, sticky="w")

    lblAddress = Label(employees_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    txtAddress = Text(employees_frame, width=85, height=5, font=("Calibri", 16))
    txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

    def getEmployeeData(event):
        selected_row = tv.focus()
        data = tv.item(selected_row)
        global row
        row = data["values"]
        #print(row)
        name.set(row[1])
        age.set(row[2])
        doj.set(row[3])
        email.set(row[4])
        gender.set(row[5])
        contact.set(row[6])
        txtAddress.delete(1.0, END)
        txtAddress.insert(END, row[7])

    def displayAllEmployees():
        tv.delete(*tv.get_children())
        for row in db.fetch_employees():
            tv.insert("", END, values=row)

    def add_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
                1.0, END) == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.insert_employee(
            txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(), txtAddress.get(
                1.0, END))
        messagebox.showinfo("Success", "Record Inserted")
        clearAll()
        displayAllEmployees()

    def update_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
                1.0, END) == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.update_employee(row[0], txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
                           txtAddress.get(1.0, END))
        messagebox.showinfo("Success", "Record Update")
        clearAll()
        displayAllEmployees()

    def delete_employee():
        db.remove_employee(row[0])
        clearAll()
        displayAllEmployees()

    def clearAll():
        name.set("")
        age.set("")
        doj.set("")
        gender.set("")
        email.set("")
        contact.set("")
        txtAddress.delete(1.0, END)

    btn_frame = Frame(employees_frame, bg="#535c68")
    btn_frame.grid(row=6, column=0, columnspan=4, pady=10)
    
    btnAdd = Button(btn_frame, command=add_employee, text="Add Employee", width=15, font=("Calibri", 16, "bold"), fg="white",
                    bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_employee, text="Update Employee", width=15, font=("Calibri", 16, "bold"),
                     fg="white", bg="#2980b9",
                     bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_employee, text="Delete Employee", width=15, font=("Calibri", 16, "bold"),
                       fg="white", bg="#c0392b",
                       bd=0).grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearAll, text="Clear", width=15, font=("Calibri", 16, "bold"), fg="white",
                      bg="#f39c12",
                      bd=0).grid(row=0, column=3, padx=10)

    # Employee Table Frame
    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=480, width=1980, height=520)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="ID")
    tv.column("1", width=5)
    tv.heading("2", text="Name")
    tv.heading("3", text="Age")
    tv.heading("4", text="D.O.J")
    tv.heading("5", text="Email")
    tv.heading("6", text="Gender")
    tv.heading("7", text="Contact")
    tv.heading("8", text="Address")
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", getEmployeeData)
    tv.pack(fill=X)

    displayAllEmployees()

# Departments Frame
def departments_frame():
    departments_frame = Frame(root, bg="#535c68")
    departments_frame.pack(side=TOP, fill=X)

    lblDepartmentName = Label(departments_frame, text="Department Name", font=("Calibri", 16), bg="#535c68", fg="white")
    lblDepartmentName.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    txtDepartmentName = Entry(departments_frame, textvariable=department_name, font=("Calibri", 16), width=30)
    txtDepartmentName.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    def getDepartmentData(event):
        selected_row = department_tv.focus()
        data = department_tv.item(selected_row)
        global row
        row = data["values"]
        department_name.set(row[1])

    def displayAllDepartments():
        department_tv.delete(*department_tv.get_children())
        for row in db.fetch_departments():
            department_tv.insert("", END, values=row)

    def add_department():
        if txtDepartmentName.get() == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.insert_department(txtDepartmentName.get())
        messagebox.showinfo("Success", "Record Inserted")
        clearAllDepartments()
        displayAllDepartments()

    def update_department():
        if txtDepartmentName.get() == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.update_department(row[0], txtDepartmentName.get())
        messagebox.showinfo("Success", "Record Updated")
        clearAllDepartments()
        displayAllDepartments()

    def delete_department():
        db.remove_department(row[0])
        clearAllDepartments()
        displayAllDepartments()

    def clearAllDepartments():
        department_name.set("")

    btn_frame = Frame(departments_frame, bg="#535c68")
    btn_frame.grid(row=2, column=0, columnspan=4, pady=10)

    btnAdd = Button(btn_frame, command=add_department, text="Add Department", width=15, font=("Calibri", 16, "bold"), fg="white",
                    bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_department, text="Update Department", width=15, font=("Calibri", 16, "bold"),
                     fg="white", bg="#2980b9",
                     bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_department, text="Delete Department", width=15, font=("Calibri", 16, "bold"),
                       fg="white", bg="#c0392b",
                       bd=0).grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearAllDepartments, text="Clear", width=15, font=("Calibri", 16, "bold"), fg="white",
                      bg="#f39c12",
                      bd=0).grid(row=0, column=3, padx=10)

    # Departments Table Frame
    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=480, width=1980, height=520)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    department_tv = ttk.Treeview(tree_frame, columns=(1, 2), style="mystyle.Treeview")
    department_tv.heading("1", text="ID")
    department_tv.column("1", width=5)
    department_tv.heading("2", text="Department Name")
    department_tv['show'] = 'headings'
    department_tv.bind("<ButtonRelease-1>", getDepartmentData)
    department_tv.pack(fill=X)

    displayAllDepartments()

# Salaries Frame
def salaries_frame():
    salaries_frame = Frame(root, bg="#535c68")
    salaries_frame.pack(side=TOP, fill=X)

    lblEmployeeID = Label(salaries_frame, text="Employee ID", font=("Calibri", 16), bg="#535c68", fg="white")
    lblEmployeeID.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    txtEmployeeID = Entry(salaries_frame, textvariable=salary_amount, font=("Calibri", 16), width=30)
    txtEmployeeID.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    lblSalaryAmount = Label(salaries_frame, text="Salary Amount", font=("Calibri", 16), bg="#535c68", fg="white")
    lblSalaryAmount.grid(row=0, column=2, padx=10, pady=10, sticky="w")
    txtSalaryAmount = Entry(salaries_frame, textvariable=salary_amount, font=("Calibri", 16), width=30)
    txtSalaryAmount.grid(row=0, column=3, padx=10, pady=10, sticky="w")

    def getSalaryData(event):
        selected_row = salary_tv.focus()
        data = salary_tv.item(selected_row)
        global row
        row = data["values"]
        salary_amount.set(row[2])

    def displayAllSalaries():
        salary_tv.delete(*salary_tv.get_children())
        for row in db.fetch_salaries():
            salary_tv.insert("", END, values=row)

    def add_salary():
        if txtEmployeeID.get() == "" or txtSalaryAmount.get() == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.insert_salary(txtEmployeeID.get(), txtSalaryAmount.get())
        messagebox.showinfo("Success", "Record Inserted")
        clearAllSalaries()
        displayAllSalaries()

    def update_salary():
        if txtEmployeeID.get() == "" or txtSalaryAmount.get() == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.update_salary(row[0], txtEmployeeID.get(), txtSalaryAmount.get())
        messagebox.showinfo("Success", "Record Updated")
        clearAllSalaries()
        displayAllSalaries()

    def delete_salary():
        db.remove_salary(row[0])
        clearAllSalaries()
        displayAllSalaries()

    def clearAllSalaries():
        salary_amount.set("")

    btn_frame = Frame(salaries_frame, bg="#535c68")
    btn_frame.grid(row=2, column=0, columnspan=4, pady=10)

    btnAdd = Button(btn_frame, command=add_salary, text="Add Salary", width=15, font=("Calibri", 16, "bold"), fg="white",
                    bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_salary, text="Update Salary", width=15, font=("Calibri", 16, "bold"),
                     fg="white", bg="#2980b9",
                     bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_salary, text="Delete Salary", width=15, font=("Calibri", 16, "bold"),
                       fg="white", bg="#c0392b",
                       bd=0).grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearAllSalaries, text="Clear", width=15, font=("Calibri", 16, "bold"), fg="white",
                      bg="#f39c12",
                      bd=0).grid(row=0, column=3, padx=10)

    # Salaries Table Frame
    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=480, width=1980, height=520)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    salary_tv = ttk.Treeview(tree_frame, columns=(1, 2, 3), style="mystyle.Treeview")
    salary_tv.heading("1", text="ID")
    salary_tv.column("1", width=5)
    salary_tv.heading("2", text="Employee ID")
    salary_tv.heading("3", text="Salary Amount")
    salary_tv['show'] = 'headings'
    salary_tv.bind("<ButtonRelease-1>", getSalaryData)
    salary_tv.pack(fill=X)

    displayAllSalaries()

# Projects Frame
def projects_frame():
    projects_frame = Frame(root, bg="#535c68")
    projects_frame.pack(side=TOP, fill=X)

    lblProjectName = Label(projects_frame, text="Project Name", font=("Calibri", 16), bg="#535c68", fg="white")
    lblProjectName.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    txtProjectName = Entry(projects_frame, textvariable=project_name, font=("Calibri", 16), width=30)
    txtProjectName.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    lblEmployeeID = Label(projects_frame, text="Employee ID", font=("Calibri", 16), bg="#535c68", fg="white")
    lblEmployeeID.grid(row=0, column=2, padx=10, pady=10, sticky="w")
    txtEmployeeID = Entry(projects_frame, textvariable=project_employee_id, font=("Calibri", 16), width=30)
    txtEmployeeID.grid(row=0, column=3, padx=10, pady=10, sticky="w")

    def getProjectData(event):
        selected_row = project_tv.focus()
        data = project_tv.item(selected_row)
        global row
        row = data["values"]
        project_name.set(row[1])
        project_employee_id.set(row[2])

    def displayAllProjects():
        project_tv.delete(*project_tv.get_children())
        for row in db.fetch_projects():
            project_tv.insert("", END, values=row)

    def add_project():
        if txtProjectName.get() == "" or txtEmployeeID.get() == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.insert_project(txtProjectName.get(), txtEmployeeID.get())
        messagebox.showinfo("Success", "Record Inserted")
        clearAllProjects()
        displayAllProjects()

    def update_project():
        if txtProjectName.get() == "" or txtEmployeeID.get() == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.update_project(row[0], txtProjectName.get(), txtEmployeeID.get())
        messagebox.showinfo("Success", "Record Updated")
        clearAllProjects()
        displayAllProjects()

    def delete_project():
        db.remove_project(row[0])
        clearAllProjects()
        displayAllProjects()

    def clearAllProjects():
        project_name.set("")
        project_employee_id.set("")

    btn_frame = Frame(projects_frame, bg="#535c68")
    btn_frame.grid(row=2, column=0, columnspan=4, pady=10)

    btnAdd = Button(btn_frame, command=add_project, text="Add Project", width=15, font=("Calibri", 16, "bold"), fg="white",
                    bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_project, text="Update Project", width=15, font=("Calibri", 16, "bold"),
                     fg="white", bg="#2980b9",
                     bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_project, text="Delete Project", width=15, font=("Calibri", 16, "bold"),
                       fg="white", bg="#c0392b",
                       bd=0).grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearAllProjects, text="Clear", width=15, font=("Calibri", 16, "bold"), fg="white",
                      bg="#f39c12",
                      bd=0).grid(row=0, column=3, padx=10)

    # Projects Table Frame
    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=480, width=1980, height=520)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    project_tv = ttk.Treeview(tree_frame, columns=(1, 2, 3), style="mystyle.Treeview")
    project_tv.heading("1", text="ID")
    project_tv.column("1", width=5)
    project_tv.heading("2", text="Project Name")
    project_tv.heading("3", text="Employee ID")
    project_tv['show'] = 'headings'
    project_tv.bind("<ButtonRelease-1>", getProjectData)
    project_tv.pack(fill=X)

    displayAllProjects()

# Adding Menu
menu = Menu(root)
root.config(menu=menu)

# Adding Employee Menu Item
employee_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Employees", menu=employee_menu)
employee_menu.add_command(label="Manage Employees", command=employees_frame)

# Adding Department Menu Item
department_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Departments", menu=department_menu)
department_menu.add_command(label="Manage Departments", command=departments_frame)

# Adding Salary Menu Item
salary_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Salaries", menu=salary_menu)
salary_menu.add_command(label="Manage Salaries", command=salaries_frame)

# Adding Project Menu Item
project_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Projects", menu=project_menu)
project_menu.add_command(label="Manage Projects", command=projects_frame)

root.mainloop()