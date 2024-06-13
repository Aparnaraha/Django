from django.db import models

# Create your models here.
class company(models.Model):
  company_id = models.IntegerField
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=50)


class Employee(models.Model):
  employee_id = models.IntegerField
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100) 
  salary = models.FloatField