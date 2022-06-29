from django.forms import Form, CharField, FloatField

class AddStudentForm(Form):
    name = CharField(label='Name', max_length=50)
    grades = CharField(label='Grades', max_length=100)
    #average_grade = FloatField(label='Average grade')