
class Department:
    """Model object for a department, including code, name, and director DNI."""

    def __init__(self,cod_d,depName,depDirdni):
        """Initialize a Department with code, name, and optional director DNI."""
        self.__cod_d = cod_d            # PK not nul
        self.__depName = depName        # not null
        self.__depDirdni = depDirdni    # NULL
    
    def __str__(self):
        """Return a readable Department string representation."""
        return f"Department: {self.__cod_d}, Name: {self.__depName}, Director DNI: {self.__depDirdni}"

    def depCode(self):
        """Return the department code."""
        return self.__cod_d
    
    @property
    def depName(self):
        """Get the department name."""
        return self.__depName
    @depName.setter
    def depName(self, novo_nome):
        """Set a new department name, requiring more than two characters."""
        if len(novo_nome) > 2:
          self.__depName = novo_nome
        else:
          print("The name has to be more than 2 caracters! ")
    
    @property
    def depDirdni(self):
        """Get the director's DNI for the department."""
        return self.__depDirdni
    @depDirdni.setter
    def depDirdni(self, new_dni):
        """Set the department director DNI, validating a 9-character DNI string."""
        if len(new_dni) == 9:
          self.__depDirdni = new_dni
        else:
          print("Incorrect DNI number length! ")
    

