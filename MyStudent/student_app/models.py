from django.db import models

#Izveidot modeli StudentModel, kuram ir lauki (fields): name (CharField),
# grades (CharField), average_grade (FloatField).




class Studentmodel(models.Model):

    name = models.CharField(max_length=50)
    grades = models.CharField(max_length=100)
    average_grade = models.FloatField()
