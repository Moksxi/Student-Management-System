from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    course = models.CharField(max_length=255, choices=[
        ('BS-CS', 'BS in Computer Science'),
        ('BS-DS', 'BS in Data Science'),
        ('BS-IT', 'BS in Information Technology'),
        ('BS-IS', 'BS in Information Systems'),
    ])
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ])
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"