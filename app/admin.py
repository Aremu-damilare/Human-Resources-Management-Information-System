from django.contrib import admin
from .models import Employee, Leave, LeaveType, Performance, PerformanceType, Manager, \
    Department, EmploymentStatus, Job, Salary, TrainingDuration, Training, TrainingType, \
        Recruitment, ActivityLog
# Register your models here.

admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(ActivityLog)
admin.site.register(Training)
admin.site.register(TrainingDuration)
admin.site.register(TrainingType)
admin.site.register(Salary)
admin.site.register(EmploymentStatus)
admin.site.register(Manager)
admin.site.register(Department)
admin.site.register(Leave)
admin.site.register(LeaveType)
admin.site.register(Performance)
admin.site.register(PerformanceType)
