class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
       
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average(self):
        all_rates = [rate for rates in self.grades.values() for rate in rates]
        return round(sum(all_rates) / len(all_rates), 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашее задание: {self.__average()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить')
            return
        return self.__average() < other.__average()
       
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def __average(self):
        all_rates = [rate for rates in self.grades.values() for rate in rates]
        return round(sum(all_rates) / len(all_rates), 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.__average()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить')
            return
        return self.__average() < other.__average()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

student_1 = Student('Мария', 'Иванова', 'ж')
student_1.finished_courses += ['Git']
student_1.courses_in_progress += ['Python', 'Java']

student_2 = Student('Петр', 'Сидоров', 'м')
student_2.finished_courses += ['Git']
student_2.courses_in_progress += ['Python', 'Java']

lecturer_1 = Lecturer('Светлана', 'Попова')
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Максим', 'Зайцев')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Елена', 'Петрова')
reviewer_1.courses_attached += ['Python', 'Java']

reviewer_2 = Reviewer('Дмитрий', 'Волков')
reviewer_2.courses_attached += ['Python', 'Java']

student_1.rate_lecture(lecturer_1, 'Git', 9)
student_1.rate_lecture(lecturer_2, 'Git', 10)

student_2.rate_lecture(lecturer_1, 'Git', 10)
student_2.rate_lecture(lecturer_2, 'Git', 9)

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Java', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Java', 10)

reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Java', 10)

list_students = [student_1, student_2]
list_lecturers = [lecturer_1, lecturer_2]

def student_average(list_students, course):
    res = 0
    counter = 0
    for student in list_students:
        for key, value in student.__dict__['grades'].items():
            if key == course:
                res += round(sum(value) / len(value), 2)
                counter +=1
    return f'Средняя оценка за курс {course}: {round(res / counter, 2)}'

def lecturer_average(list_lecturers, course):
    res = 0
    counter = 0
    for lecturer in list_lecturers:
        for key, value in lecturer.__dict__['grades'].items():
            if key == course:
                res += round(sum(value) / len(value), 2)
                counter +=1
            else:
                return 'Этого курса нет'
    return f'Средняя оценка за лекции по курсу {course}: {round(res / counter, 2)}'
        
print(student_1)
print(student_1 > student_2)
print(lecturer_1)
print(lecturer_1 > lecturer_2)
print(reviewer_2)
print(student_average(list_students, 'Python'))
print(lecturer_average(list_lecturers, 'Git'))