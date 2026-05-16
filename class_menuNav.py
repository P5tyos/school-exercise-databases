from class_DBmySQL import *
from class_DBsqLite import *

class MenuNav:
    """Menu navigation utilities for the SXED application."""

    def select_DB():
        """Prompt the user to choose MySQL or SQLite and return the selected DB class, connection, and cursor."""
        print("Please select the database you want to use: ")
        print("     1. MySQL")
        print("     2. SQLite")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                conn, cursor = DBmySQL.connectMySQL()
                DBmySQL.createTables(cursor)
                return DBmySQL, conn, cursor  #returns 3 var: first one is to identify the DB class
            case "2":
                conn, cursor = DBsqLite.connectLite()
                DBsqLite.createTables(cursor)
                return DBsqLite, conn, cursor
            case _:
                print("Invalid option! Please try again.")
                return MenuNav.select_DB()

    def mostrar_menu_principal():
        """Print the main menu options for department and employee management."""
        print("\nPlease select an option: ")
        print("     1. Manage Departments")
        print("     2. Manage Employees")
        print("     3. Exit")

    def menu_departments():
        """Print the department submenu options."""
        print("\nPlease select an option: ")
        print("     1. Create Department")
        print("     2. Update Department")
        print("     3. Delete Department")
        print("     4. Show Department by Name")
        print("     5. Show All Departments")
        print("     6. Return to Main Menu")

    def menu_employees():
        """Print the employee submenu options."""
        print("\nPlease select an option: ")
        print("     1. Create Employee")
        print("     2. Update Employee")
        print("     3. Delete Employee")
        print("     4. Show All Employees")
        print("     5. Show Employees by Department")
        print("     6. Return to Main Menu")