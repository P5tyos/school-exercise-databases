import sqlite3
from class_department import*
from class_employee import *

class DBsqLite:
    """SQLite backend implementation for department and employee management."""

    def connectLite():
        """Connect to a local SQLite database and return the connection and cursor."""
        conn = sqlite3.connect("sxed.db") 
        conn.execute("PRAGMA foreign_keys = ON")  # Activa o modo FOREIGN_KEYS
        cursor = conn.cursor()
        return conn, cursor

    def createTable(cursor, tableName):
        """Create a SQLite table by name identifier: 1 for Department, 2 for Employee."""
        if tableName == 1:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Department (
                    cod_d INTEGER PRIMARY KEY AUTOINCREMENT,
                    depName varchar(20) NOT NULL,
                    depDirdni char(9) NULL
                
                )
            """) #    FOREIGN KEY (depDirdni) REFERENCES Employee(dni)
        elif tableName == 2:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Employee (
                    dni char(9) PRIMARY KEY,
                    empName varchar(20) NOT NULL,
                    salary int NOT NULL,
                    dprtmnt integer NULL REFERENCES Department(cod_d)
                )
            """)
        else:
            print("Incorrect table name.")
    def createTables(cursor):
        """Create the required Department and Employee tables in SQLite."""
        DBsqLite.createTable(cursor, 1)
        DBsqLite.createTable(cursor, 2)
    def commitChanges(conn):
        conn.commit()

    def closeConnection(conn):
        """Close the SQLite database connection."""
        conn.close()
    
    def searchEmpl(cursor,dni):
        """Search for an employee by DNI and return matching rows or None."""
        cursor.execute("SELECT dni from Employee where dni = ?",(dni,))
        results = cursor.fetchall()
        return results if results else None

    def searchDepByName(cursor, depName):
        """Search the Department table by name and print the result if found."""
        cursor.execute("SELECT cod_d, depName, depDirdni FROM Department WHERE depName = ?", (depName,))
        result = cursor.fetchone() 
        if result:
            DBsqLite.showDepartmentSQL(cursor, result)
        return result if result else None 

    def showDepartmentSQL(cursor, eachDep):
        """Print department details for a department tuple or Department object."""
        if hasattr(eachDep, 'depName'):
            depName = eachDep.depName
            cod_d = eachDep.depCode()
            depDirdni = eachDep.depDirdni
        else:
            depName = eachDep[1]
            cod_d = eachDep[0]
            depDirdni = eachDep[2]
        print(f"We have found a Department called {depName}, with code {cod_d}, directed by employee with DNI: {depDirdni}.")

    def searchDepByCode(cursor):
        """Prompt for a department code and display the matching SQLite record."""
        code = input("Please enter the department's code: ")
        try:
            code = int(code)
        except ValueError:
            print("Department code must be a number.")
            return None
        cursor.execute("SELECT * FROM Department WHERE cod_d = ?", (code,))
        result = cursor.fetchone()
        if result:
            DBsqLite.showDepartmentSQL(cursor, result)
            return result
        else:
            print("Couldn't find a department with this code.")
            return None
    
    def insertNewDep(cursor):
        """Prompt for department data and insert a new department into SQLite."""
        depName = input("Please enter the name of the Department: ")
        foundDep=DBsqLite.searchDepByName(cursor,depName)
        if foundDep:
            print('Error! Department already exists. ')
        else:
            depDirdni = input("Please enter the DNI of the responsible of the department if known: ")
            if depDirdni:
                depDirdni = depDirdni.strip()
                if depDirdni.lower() == 'null':
                    depDirdni = None
                else:
                    found = DBsqLite.searchEmpl(cursor, depDirdni)
                    if not found:
                        input(f"No employee has been found with dni: {depDirdni}")
                        depDirdni = None
            else:
                depDirdni = None
            doubleCheck = input(f"Are you sure you'd like to create the new department: {depName}? y/n ")
            if doubleCheck == 'y':
                cursor.execute("SELECT COALESCE(MAX(cod_d), 0) FROM Department")
                max_cod_d = cursor.fetchone()  # This will be an integer (0 if no rows)
                DepCode = max_cod_d[0] + 1
                newDep = Department(DepCode,depName,depDirdni)   #se crea el obxecto
                cursor.execute("INSERT INTO Department (cod_d, depName, depDirdni) VALUES (?, ?, ?)", (newDep.depCode(), newDep.depName, newDep.depDirdni))
                print("Successfully inserted a new depatment! ")

    
    def insertNewEmpl(cursor):
        """Prompt for employee data and insert a new employee into SQLite."""
        #cursor.execute("insert into Employee (dni,empName,salary) Values('12346578D','Janny',1750)")
        emplDNI=input("Please enter the employee's DNI: ")    #get DNI
        foundEmpl = DBsqLite.searchEmpl(cursor,emplDNI)       #check if already exists
        if foundEmpl == None:
            emplName=input("Please enter the employee's name: ")   #get name
            emplSalary = round(float(input("Please enter the employee's salary: ")), 2)   #get salary and round it to 2 decimals
            foundDep = None
            while foundDep == None:
                depPertenece = input("Please enter the NAME of the employee's Department: ")   #get dep name
                foundDep = DBsqLite.searchDepByName(cursor,depPertenece)       #check if it exists
                if foundDep == None:                               
                    print("Couldn't find a Department with name:"+depPertenece+" Please try again! ")  #if it doesn't, try again
            print(emplDNI,emplName,emplSalary,foundDep[0])
            newEmpl = Employee(emplDNI,emplName,emplSalary,foundDep[0])
            cursor.execute("INSERT INTO Employee (dni, empName, salary, dprtmnt) \
                           VALUES (?,?,?,?)",(newEmpl.empDni(),newEmpl.empName,newEmpl.salary,newEmpl.depPert))
            print("Successfully inserted a new employee! ")
                
    def showAllDep(cursor):
        """Retrieve and print all departments from SQLite."""
        lisataDepartamentosAsObjects = []
        cursor.execute("select * from Department")
        results = cursor.fetchall()
        if not results:
            print("No departments found.")
            return []
        print("We have found the following departments: ")
        for each in results:
            newDep = Department(cod_d=each[0],depName=each[1],depDirdni=each[2])
            lisataDepartamentosAsObjects.append(newDep)
            DBsqLite.showDepartmentSQL(cursor, each)
        return lisataDepartamentosAsObjects

    def showEmployee(cursor, eachEmployee):
        """Print employee details for a tuple or Employee object."""
        # eachEmployee may be a tuple with (dni, name, salary) or (dni, name, salary, department)
        try:
            dni = eachEmployee[0]
            name = eachEmployee[1]
            salary = eachEmployee[2]
            dept = eachEmployee[3] if len(eachEmployee) > 3 else None
        except Exception:
            # If passed an Employee object, attempt to read attributes
            dni = getattr(eachEmployee, 'empDni', lambda: None)()
            name = getattr(eachEmployee, 'empName', None)
            salary = getattr(eachEmployee, 'salary', None)
            dept = getattr(eachEmployee, 'depPert', None)
        dept_str = dept if dept is not None else 'N/A'
        print(f"DNI: {dni}, Name: {name}, Salary: {salary}, Department: {dept_str}")

    def showAllEmpl(cursor):
        """Retrieve and print all employees from SQLite."""
        listaEmpleadosAsObjects = []
        cursor.execute("select * from Employee")
        result = cursor.fetchall()
        if not result:
            print("No employees found.")
            return []
        for each in result:
            newEmpl = Employee(dni=each[0],empName=each[1],salary=each[2],department=each[3])
            listaEmpleadosAsObjects.append(newEmpl)
            DBsqLite.showEmployee(cursor, each)
        return listaEmpleadosAsObjects

    def showEmplByDep(cursor,depName):
        """Retrieve and print SQLite employees for a given department."""
        # include department name as the 4th column so showEmployee can display it
        cursor.execute("SELECT e.dni, e.empName, e.salary, d.depName FROM Employee e JOIN Department d ON e.dprtmnt = d.cod_d WHERE d.depName = ?", (depName,))
        result = cursor.fetchall()
        if result:
            print(f"Employees in department {depName}:")
            for emp in result:
                DBsqLite.showEmployee(cursor, emp)
        else:
            print(f"No employees found in department {depName}.")
        return result

    def updateDep(cursor):
        """Prompt the user to update a department's name or director DNI in SQLite."""
        depName = input("Please enter the name of the department you want to update: ")
        choice=int(input("To update it's name: enter 1. To update the director's DNI enter 2: "))
        foundDep = DBsqLite.searchDepByName(cursor, depName)
        if foundDep:
            if choice == 1:     #update department's name
                newName = input("Please enter the new name for the department: ")
                cursor.execute("UPDATE Department SET depName = ? WHERE cod_d = ?", (newName, foundDep[0]))
                print("Department name updated successfully!")
            elif choice == 2:       #update department's director (DNI)
                newDirDni = input("Please enter the new director's DNI for the department: ")
                foundDNI = DBsqLite.searchEmpl(cursor,newDirDni)
                if not foundDNI:
                    input(f"No employee has been found with dni: {newDirDni}")
                    newDirDni = None  
                cursor.execute("UPDATE Department SET depDirdni = ? WHERE cod_d = ?", (newDirDni, foundDep[0]))
                print("Department director's DNI updated successfully!")
        else:
            print("Department not found. Please try again.")

    def updateEmpl(cursor):
        """Prompt the user to update an employee's name, salary, or department in SQLite."""
        emplDNI = input("Please enter the DNI of the employee you want to update: ")
        choice=int(input("To update the name enter 1. To update the salary, enter 2. To update the department, enter 3: "))
        foundEmpl = DBsqLite.searchEmpl(cursor, emplDNI)    #check if employee exists
        if foundEmpl:
            match choice:
                case 1:       #update employee's name
                    newName = input("Please enter the new name for the employee: ")
                    cursor.execute("UPDATE Employee SET empName = ? WHERE dni = ?", (newName, emplDNI))
                    print("Employee name updated successfully!")
                    cursor.execute("SELECT * FROM Employee WHERE dni = ?", (emplDNI,))
                    updatedEmpl = cursor.fetchone()
                    if updatedEmpl:
                        DBsqLite.showEmployee(cursor, updatedEmpl)
                case 2:     #update employee's salary   
                    newSalary = float(input("Please enter the new salary for the employee: "))
                    cursor.execute("UPDATE Employee SET salary = ? WHERE dni = ?", (newSalary, emplDNI))
                    print("Employee salary updated successfully!")
                    cursor.execute("SELECT * FROM Employee WHERE dni = ?", (emplDNI,))
                    updatedEmpl = cursor.fetchone()
                    if updatedEmpl:
                        DBsqLite.showEmployee(cursor, updatedEmpl)
                case 3:      #update employee's department
                    newDep = input("Please enter the new department for the employee: ")
                    foundDep = DBsqLite.searchDepByName(cursor, newDep)
                    if foundDep:
                        cursor.execute("UPDATE Employee SET dprtmnt = ? WHERE dni = ?", (foundDep[0], emplDNI))
                        print("Employee department updated successfully!")
                    else:
                        print("Department not found. Employee department was not updated.")
        else:
            print("Employee not found. Please try again.")

    def deleteDep(cursor):
        """Delete a department in SQLite, optionally reassigning or clearing its employees."""
        depName = input("Please enter the name of the department you want to delete: ")
        foundDep = DBsqLite.searchDepByName(cursor, depName)   #check if the department exists
        if foundDep:   
            listEmplByDep = DBsqLite.showEmplByDep(cursor,depName)   #check if there are employees assigned to the department
            if listEmplByDep:
                print("This department has employees assigned to it. Befor deleting the department you have to: ")
                choice=int(input("Reassign them to another department (enter 1). \n Leave them without department (enter 2).\n Or cancel operation (enter 3): "))
                match choice:
                    case 1:     #reassign employees to another department
                        newDep = input("Please enter the name of the department you want to reassign the employees to: ")
                        foundNewDep = DBsqLite.searchDepByName(cursor, newDep)      #check if the new department exists 
                        if foundNewDep:
                            cursor.execute("UPDATE Employee SET dprtmnt = ? WHERE dprtmnt = ?", (foundNewDep[0], foundDep[0]))
                            print("Employees reassigned successfully!")
                            cursor.execute("SELECT e.dni, e.empName, e.salary, d.depName FROM Employee e JOIN Department d ON e.dprtmnt = d.cod_d WHERE d.depName = ?", (newDep,))
                            result = cursor.fetchall()
                            print(f"Employees in department {newDep}:")
                            for emp in result:
                                DBsqLite.showEmployee(cursor, emp)
                        else:
                            choice=int(input("Couldn't find a department with this name. Would you like to set it to NULL? (enter 2) \
                                             Or cancel operation (enter 3): "))
                                    
                    case 2:     #update employees' department to NULL
                        cursor.execute("UPDATE Employee SET dprtmnt = NULL WHERE dprtmnt = ?", (foundDep[0],))
                        print("Employees department set to NULL successfully!")
                    case 3:     #cancel operation
                        print("Department deletion cancelled.")
                        return
            cursor.execute("DELETE FROM Department WHERE cod_d = ?", (foundDep[0],))
            print("Department deleted successfully!") 
        else:
            print("Department not found. Please try again.")
        
    def deleteEmpl(cursor):
        """Prompt to delete an employee in SQLite, handling department director reassignment if needed."""
        emplDNI = input("Please enter the DNI of the employee you want to delete: ")
        foundEmpl = DBsqLite.searchEmpl(cursor, emplDNI)         #check if employee exists
        if foundEmpl:
            cursor.execute("SELECT cod_d FROM Department WHERE depDirdni = ?", (emplDNI,))        #check if employee is a director of any department
            result = cursor.fetchone()
            if result: 
                print(f"This employee is the director of department with code {result[0]}. Before deleting the employee you have to: ")
                choice=int(input("Assign a new director to the department (enter 1). \
                                    Leave the department without director (enter 2). Or cancel operation (enter 3): "))
                match choice:
                    case 1:         #assign a new director to the department
                        newDirDni = input("Please enter the DNI of the new director for the department: ")
                        foundDNI = DBsqLite.searchEmpl(cursor,newDirDni)    #check if the new director exists
                        if not foundDNI:
                            input(f"No employee has been found with dni: {newDirDni}")     #assign NULL if the new director doesn't exist
                            newDirDni = None  
                        cursor.execute("UPDATE Department SET depDirdni = ? WHERE cod_d = ?", (newDirDni, result[0]))    #update the department with the new director's DNI
                        print("Department director's DNI updated successfully!")  
                    case 2:     #update the department's director DNI to NULL
                        cursor.execute("UPDATE Department SET depDirdni = NULL WHERE cod_d = ?", (result[0],))    
                        print("Department director's DNI set to NULL successfully!")
                    case 3:     #cancel operation
                        print("Employee deletion cancelled.")
                        return
            cursor.execute("DELETE FROM Employee WHERE dni = ?", (emplDNI,))  #delete the employee (as it wasn´t director or after updating the department's director)
            print("Employee deleted successfully!")
        else:
            print("Employee not found. Please try again.")

