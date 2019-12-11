 
class Employee(object):
    rise_amount = 1.04
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName+lastName+'@email.com'
    
    def fullName(self):
        return '{} {}'.format(self.firstName,self.lastName)
    
    @classmethod
    def calHike(cls):
        pass

class Developer(Employee):
    def __init__(self,firstName,lastName,pay):
        super(Developer,self).__init__(firstName,lastName)
        self.pay = pay


class Manager(Employee):
    def __init__(self,firstName,lastName,employeeList=None):
        super(Manager,self).__init__(firstName,lastName)
        if employeeList is None:
            self.employeeList = []
        else:
            self.employeeList = employeeList
    
    def add_emp(self,emp):
        self.employeeList.append(emp)
    
    def remove_emp(self,emp):
        self.employeeList.remove(emp)

    def getEmployeeList(self):
        
        if self.employeeList is not None:
            print('Employees tagged to {} are'.format(self.fullName()))
            for emp in self.employeeList:
                print(emp.fullName())
        else:
            print('None are tagged to {}'.format(self.fullName()))

         

dev1 = Developer('Tejesh','Gangari',1000)
dev2 = Developer('Amrutha','Varshini',1000)
mgr1 = Manager('Tejesh','Kumar')
mgr2 = Manager('Amrutha','Bulagonda')
mgr1.add_emp(dev1)
mgr1.add_emp(dev2)
mgr1.getEmployeeList()
mgr2.getEmployeeList()