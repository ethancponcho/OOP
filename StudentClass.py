class Student:
    
    def __init__(self):
        self.studentid = 8915555
        self.name = 'John Smith'
        self.dob = 2000
        self.classification = 'Junior'
        self.register = ''
        
    def calc_age(self):
        self.dob = 2024 - self.dob
        
    def determine_register_date(self):
        if self.classification == 'Senior':
            self.register = '4/1 thru 4/3'
        elif self.classification == 'Junior':
            self.register = '4/4 thru 4/6'
        elif self.classification == 'Sophomore':
            self.register = '4/7 thru 4/9'
        elif self.classification == 'Freshman':
            self.register = '4/10 thru 4/9'
        else:
            self.register = 'Student Cannot Register.'
        
    def get_age(self):
        return self.dob
    
    def get_register_date(self):
        return self.register
    
    def get_studentid(self):
        return self.studentid
    
    def get_name(self):
        return self.name
    
    def get_class(self):
        return self.classification