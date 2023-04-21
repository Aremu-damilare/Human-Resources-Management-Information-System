from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model



class Department(models.Model):
    department_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department_name

class Position(models.Model):
    position_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.position_name
        
class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class TrainingDuration(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class TrainingType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        
class EmploymentStatus(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class PerformanceType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Salary(models.Model):    
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2)
    salary_start_date = models.DateField()
    
    def __str__(self):
        return str(self.salary_amount)





class Job(models.Model):
    title = models.CharField(max_length=100)
    ####### department = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True)
    description = models.TextField(null=True)
    date_posted = models.DateField(null=True)
    closing_date = models.DateField(null=True)

    def __str__(self):
        return self.title



class Manager(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, unique=True)
    contact_number = models.CharField(max_length=15, null=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.email


class Employee(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Female')
    nationality = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100,  unique=True)
    address = models.CharField(max_length=200)
    employment_status = models.ForeignKey(EmploymentStatus, on_delete=models.SET_NULL, null=True)
    employment_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    salary_amount = models.ForeignKey('Salary', on_delete=models.SET_NULL, null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return str(self.email)
      


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    # choices
    leave_type = models.ForeignKey(LeaveType, on_delete=models.SET_NULL, null=True)
    
    start_date = models.DateField()
    end_date = models.DateField()
    approval_status = models.BooleanField(default=False)

    def __str__(self):
        return self.employee

class Training(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    # choices
    training_type = models.ForeignKey(TrainingType, on_delete=models.SET_NULL, null=True)
    
    training_date = models.DateField()
    training_location = models.CharField(max_length=200)
    training_duration = models.ForeignKey(TrainingDuration, on_delete=models.SET_NULL, null=True)


class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    # choices
    performance_type = models.ForeignKey(PerformanceType, on_delete=models.SET_NULL, null=True)
    
    performance_date = models.DateField()
    performance_score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.employee)


class Recruitment(models.Model):
    recruitment_id = models.AutoField(primary_key=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    Job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateField()
    closing_date = models.DateField()
    
    

class ActivityLog(models.Model):
    activity = models.TextField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)    
    message = models.CharField(max_length=255)    
    timestamp = models.DateTimeField(auto_now_add=True)