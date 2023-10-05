class Student:
    def __init__(self,name,cls,id) -> None:
        self.name =name
        self.id = id
        self.cls = cls

    def __repr__(self) -> str:
        return f'Students with name: {self.name}, class:{self.cls}, id: {self.id}'
    

class Teacher:
    def __init__(self,name,subject,id) -> None:
        self.name = name
        self.subject = subject
        self.id = id


    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject:{self.subject}'

class Schoool:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []


    def add_teacher(self,name,subject):
        id= len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)


    def enroll(self,name,fee):

        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) +1 
            student = Student(name, 'c', id )
            self.students.append(student)
            return f'{name} is enrolled id:{id}, extra money:{fee - 6500}'
        

    def __repr__(self) -> str:
        print('Welcome to',self.name)
        print('--------OUR Teachers------------')
        for teacher in self.teachers:
            print(teacher)
        print('-------OUR Students----------')
        for student in self.students:
            print(student)
            
            return 'ALL Done'

       

        


# alia = Student ('Alia',9,1 )
# ranbeer = Teacher('ranbeer','Alg',1)
# print(alia)
# print(ranbeer)

pihtron  =Schoool('Pihtron')
pihtron.enroll('alia',5200)
pihtron.enroll('rani',8000)
pihtron.enroll('alaws',7000)
pihtron.enroll('vaijan',90000)


pihtron.add_teacher('Tom','Alg')
pihtron.add_teacher('Decap','DS')
pihtron.add_teacher('Aj','Database')

print(pihtron)
