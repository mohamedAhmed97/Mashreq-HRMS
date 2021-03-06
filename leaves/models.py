from django.db import models
from employees.models import User
from datetime import timedelta
# Create your models here.


class LeaveMaster(models.Model):
    leave_name = models.CharField(max_length=55)
    leave_value = models.IntegerField()

    def __str__(self):
        return self.leave_name


class EmployeeLevel(models.Model):
    CONFIRM_CHOICE = (
        ('w', 'waiting'),
        ('a', 'accepted'),
        ('r', 'rejected')
    )
    emp_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    leave_id = models.ForeignKey(LeaveMaster, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    confirm = models.CharField(
        max_length=1,
        choices=CONFIRM_CHOICE,
        default='w',
        blank=True,
        null=True,
    )

    def calculate_number_of_days(self):
        return int((self.end_date - self.start_date).days)

    def calculate_resume_date(self):
        return self.end_date + timedelta(self.calculate_number_of_days())

    def check_balance(self):
        if self.emp_id.balance > self.calculate_number_of_days():
            return True
        else:
            return False

    def __str__(self):
        return self.emp_id
