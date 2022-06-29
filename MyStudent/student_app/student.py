#zveidot klasi Student,
# kurai ir atribūti name (studenta vārds), grades (studenta atzīmes),
# klasei ir metode get_average_grade(), kas aprēķina vidējo atzīmi.


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def add_grades (self):
        self.grades = []
        self.grades_int_list = list(map(int, grades_str.split(',')))
        self.grades.append(grades_int_list)

    def get_average_grade(self):
        if len(self.grades) != 0:
            return sum(self.grades) / len(self.grades)
        return 0



student = Student (
    name='Andris',
    grades=[7, 4, 10],
)

average = student.get_average_grade()
print(average)

# average = 7.0

#Kā pārveidot '7,10,4' par [7, 10, 4]:
#   grades_str = '7,10,4'
#   grades_int_list = list(map(int, grades_str.split(',')))
   # >>> grades_int_list = [7, 10, 4]```