from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=200)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.ForeignKey(Department,
                                   on_delete=models.PROTECT)

