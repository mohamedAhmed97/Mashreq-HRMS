from django.db import models

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=55)


class Position(models.Model):
    position_name = models.CharField(max_length=55)
