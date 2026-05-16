
class Employee:
    """Model object for an employee, including DNI, name, salary, and department."""

    def __init__(self,dni,empName, salary, department):
        """Initialize an Employee with DNI, name, salary, and department code."""
        self.__dni = dni            # PK not nul
        self.__empName = empName    # not null
        self.__salary = salary      # NULL
        self.__dprtmnt = department # FK !NULL!
    
    def __str__(self):
        """Return a readable Employee string representation."""
        return f"Employee: {self.__dni}, Name: {self.__empName}, Salary: {self.__salary}, Department: {self.__dprtmnt}"

    def empDni(self):
        """Return the employee's DNI."""
        return self.__dni

    @property
    def empName(self):
        """Get the employee's name."""
        return self.__empName
    @empName.setter
    def empName(self, new_name):
        if len(new_name) > 2:
          self.__empName = new_name
        else:
          print("Employee's name must be more than 2 caracters! ")

    @property
    def salary(self):
        """Get the employee's salary."""
        return self.__salary
    @salary.setter
    def salary(self, new_salary):
        """Set the employee's salary if the new value is higher than the current value."""
        if self.__salary < new_salary:
          self.__salary = new_salary
        else:
          print("Employee's new salary must be more than the old! ")

    @property
    def depPert(self):
        """Get the employee's department code."""
        return self.__dprtmnt
    @depPert.setter
    def depPert(self, new_depPert):
        if self.__dprtmnt != 0:
          self.__dprtmnt = new_depPert 
        else:
          print("Error! Invalid department number! ")
