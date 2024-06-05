from django.db import models

# Create your models here.
#Employee model

class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    department=models.CharField(max_length=100)
    years_at_company=models.IntegerField()
    last_perfomance_rating=models.IntegerField()

    def __str__(self):
        return (
            f'Name: {self.name} - '
            f'Department: {self.department} - '
            f'Age: {self.age} - '
            f'Years at Company: {self.years_at_company} - '
            f'Last Performance Rating: {self.last_perfomance_rating}'
        )
    
    class Meta:
        verbose_name_plural='1. Employees'