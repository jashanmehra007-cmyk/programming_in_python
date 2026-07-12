# Create a University Management System using Classes and Inheritance
class UniversityMember():
    def __init__(self,id, name, email):    
        self.id = id
        self.name = name
        self.email = email

    def display_info(self):
        print('Id:',self.id)
        print('Name:',self.name)
        print('Email:',self.email)
         
class student(UniversityMember):
    def __init__(self,id,name,email, course, sem):
        super().__init__(id,name,email)  # super() is a built-in function that gives you access to methods and                                    
        self.course = course             # properties of a parent (superclass) from within a child (subclass).
        self.sem = sem
        self.courses = []
        
    def enroll_course(self,course_name):
        self.course = course_name
        self.courses.append(course_name)
        print(course_name, 'enrolled successfully')

    def display_info(self):
        super().display_info()
        print('Program:' , self.course)
        print('Semsester:', self.sem)
    
    def display_courses(self): 
        print('Enrolled Courses:', self.courses)

class faculty(UniversityMember):
    def __init__(self,id,name,email,department,designation):
        super().__init__(id,name,email)
        self.department = department
        self.designation = designation
        self.courses = []

    def assign_course(self,course_name):
        self.courses.append(course_name)
        print(course_name, 'assigned successfully')

    def display_courses(self): 
        print('Assigned courses:', self.courses)

class staff(UniversityMember):
    def __init__(self, id, name, email, department, role):
        super().__init__(id,name,email)
        self.department = department
        self.role = role
        self.tasks = []

    def assign_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' assigned.")
    def display_tasks(self):
        print("Assigned Tasks:", self.tasks)

#student object

student1 = student(101, 'jashan','jashan123@gmailcom','Mca',3)
student1.display_info()
student1.enroll_course('python')
student1.enroll_course('Data structures')
student1.display_courses()

print('\n' + '-'* 30)

# Faculty Object
faculty1 = faculty(201, "Dr. Sharma", "sharma@gmail.com", "Computer Science", "Professor")
faculty1.display_info()
faculty1.assign_course("Python")
faculty1.assign_course("Machine Learning")
faculty1.display_courses()

print("/n" + "-" * 30)


#staff object

staff1 = staff(301, 'aman','aman@gmail.com','administration','clerk')
staff1.display_info()
staff1.assign_task('prepare reports')
staff1.assign_task('manage records')
staff1.display_tasks()





    
