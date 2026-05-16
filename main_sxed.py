"""SXED: Command-line management system for employees and departments."""

from class_menuNav import MenuNav
from class_DBmySQL import DBmySQL
from class_DBsqLite import DBsqLite


def main():
    """Launch the CLI, select the database backend, and route department/employee commands."""
    db_type, conn, cursor = MenuNav.select_DB()
    try:
        while True:
            MenuNav.mostrar_menu_principal()
            choice = input("Enter your choice: ")
            match choice:
                case "1":     # Manage Departments
                    while True:
                        MenuNav.menu_departments()
                        depChoice = input("Enter your choice: ")
                        match depChoice:
                            case "1":     # Create Department
                                db_type.insertNewDep(cursor)
                                db_type.commitChanges(conn)
                            case "2":     # Update Department
                                db_type.updateDep(cursor)
                                db_type.commitChanges(conn)
                            case "3":     # Delete Department
                                db_type.deleteDep(cursor)
                                db_type.commitChanges(conn)
                            case "4":     # Show Department by Name
                                depName = input("Please enter the name of the department to show: ")
                                db_type.searchDepByName(cursor, depName)
                            case "5":     # Show All Departments
                                db_type.showAllDep(cursor)
                            case "6":     # Return to Main Menu
                                break
                            case _:
                                print("Invalid option! Please try again.")
                case "2":     # Manage Employees
                    while True:
                        MenuNav.menu_employees()
                        empChoice = input("Enter your choice: ")
                        match empChoice:
                            case "1":     # Create Employee
                                db_type.insertNewEmpl(cursor)
                                db_type.commitChanges(conn)
                            case "2":     # Update Employee
                                db_type.updateEmpl(cursor)
                                db_type.commitChanges(conn)
                            case "3":     # Delete Employee
                                db_type.deleteEmpl(cursor)
                                db_type.commitChanges(conn)
                            case "4":     # Show All Employees
                                db_type.showAllEmpl(cursor)
                            case "5":     # Show Employees by Department
                                depName = input("Please enter the name of the department: ")
                                db_type.showEmplByDep(cursor, depName)
                            case "6":     # Return to Main Menu
                                break
                            case _:
                                print("Invalid option! Please try again.")
                case "3":
                    print("Exiting...")
                    break
                case _:
                    print("Invalid option! Please try again.")
    finally:
        db_type.closeConnection(conn)


