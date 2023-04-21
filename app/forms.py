from django import forms
from .models import Employee, Manager, Leave, Performance, Training, Salary, Job, Recruitment

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['id']
        widgets = {
            'employment_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }
        
        


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        exclude = ['id']        
        


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        exclude = ['id']     
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
                
        
class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        exclude = ['id']                 
        widgets = {
            'performance_date': forms.DateInput(attrs={'type': 'date'}),            
        } 
        


############ 
class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        exclude = ['id']     
        widgets = {
            'salary_start_date': forms.DateInput(attrs={'type': 'date'}),            
        }            

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        exclude = ['id']     
        widgets = {
            'training_date': forms.DateInput(attrs={'type': 'date'}),            
        }                     

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['id', 'closing_date']   
        widgets = {
            'date_posted': forms.DateInput(attrs={'type': 'date'}),
            'closing_date': forms.DateInput(attrs={'type': 'date'})
        }                      

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        exclude = ['id']                         
        