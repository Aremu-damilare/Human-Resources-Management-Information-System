from django.shortcuts import render, redirect
from .models import Performance, Employee, Salary, Department, Manager, Leave, Job, Recruitment, Training, \
    ActivityLog
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from .forms import EmployeeForm, ManagerForm, LeaveForm, PerformanceForm, JobForm, RecruitmentForm, TrainingForm, SalaryForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/sign_in.html', {'form': form})



@login_required(login_url='sign_in')
def home(request):
    # Retrieve performance data from the model
    performances = Performance.objects.all()
    performances_last_created = Performance.objects.all().last()

    # Extract performance date and score for each performance record
    performance_dates = [performance.performance_date for performance in performances]
    performance_scores = [performance.performance_score for performance in performances]
    performance_user = [performance.employee.first_name for performance in performances]
   
    print(performance_dates, performance_scores)
    context = {
        'performance_dates': performance_dates,
        'performance_scores': performance_scores,
        'performance_user': performance_user,
        'performances_last_created': performances_last_created,
        'active_page': 'dashboard'
    }
    
    return render(request, 'home.html', context)


def employee_department_chart(request):
    # Retrieve data from the database
    employees = Employee.objects.all()
    departments = Department.objects.all()

    # Process the data
    department_employee_count = {}
    for department in departments:
        department_employee_count[department.department_name] = employees.filter(department=department).count()

    # Prepare data for the chart
    labels = list(department_employee_count.keys())
    data = list(department_employee_count.values())
    total = employees.count()

    # Return data as JSON response
    return JsonResponse({'labels': labels, 'data': data, 'total': total})


def employee_data(request):
    # Get all employees from the database
    employees = Employee.objects.all()

    # Create a Paginator object with employees data and set the number of employees per page to 5
    paginator = Paginator(employees, 5)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    # Get the Page object for the current page
    employees_page = paginator.get_page(page)

    # Create a list to store employee data as dictionaries
    employees_data = []
    for employee in employees_page:
        # Create a dictionary to store employee data
        employee_data = {
            'id': employee.employee_id,
            'name': f'{employee.first_name} {employee.last_name}',
            'salary': 'employee.salary',  # Assuming 'salary' is a field in the Employee model
            'country': employee.nationality,
        }
        # Append employee data to the list
        employees_data.append(employee_data)

    
    try:
        last_employee = Employee.objects.latest('employee_id')        
        last_employee_date = last_employee.employment_date
        last_employee_name = last_employee.first_name + " " +last_employee.last_name        
        # print("aaa",type(last_employee), last_employee)
    except Employee.DoesNotExist:
        last_employee = None
        
    if last_employee:
        pass
    
    # Create a dictionary to store the data to be returned as JSON
    data = {
        'employees': employees_data,
        'total_pages': paginator.num_pages,
        'current_page': employees_page.number,
        'last_employee' : last_employee_date,
        'last_employee_name' : last_employee_name
    }
    
    # Return the data as JSON response
    return JsonResponse(data)



#######
@login_required(login_url='sign_in')
def employee_list(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            # log user activity
            activity = f"{request.user.username} ==> {form.cleaned_data.get('email')}."
            ActivityLog.objects.create(activity=activity, user=request.user, message='Added Employee')
            return redirect(reverse('employee_list'))
        else:
            # Form is not valid, extract specific errors and return an error message
            error_msg = 'Employee form contains errors. Please correct them and try again.'
            for field, errors in form.errors.items():
                error_msg += f' {field}: {", ".join(errors)}'
            messages.error(request, error_msg)
            
    form = EmployeeForm()
    employees = Employee.objects.all()
    employee_count = employees.count()
    context = {'employees': employees, 'form': form, 'active_page': 'employee', 'employee_count': employee_count }
    return render(request, 'employee_list.html', context)
@login_required(login_url='sign_in')
def delete_employee(request, id):
    employee = Employee.objects.get(employee_id=id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully!')
        # log user activity
        activity = f'{request.user.username} ==> {employee.email}.'
        ActivityLog.objects.create(activity=activity, user=request.user, message='Deleted Employee')
        return redirect(reverse('employee_list'))
    context = {'employee': employee}
    return render(request, 'delete_employee.html', context)



#######
@login_required(login_url='sign_in')
def manager_list(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manager added successfully!')
            # log user activity
            activity = f"{request.user.username} ==> {form.cleaned_data.get('email')}."
            ActivityLog.objects.create(activity=activity, user=request.user, message='Added manager')        
            return redirect(reverse('manager_list'))
        else:            
            # Form is not valid, extract specific errors and return an error message
            error_msg = 'Manager form contains errors. Please correct them and try again.'
            for field, errors in form.errors.items():
                error_msg += f' {field}: {", ".join(errors)}'
            messages.error(request, error_msg)
    form = ManagerForm()
    managers = Manager.objects.all()
    managers_count = managers.count()
    context = {'managers': managers, 'form': form, 'active_page': 'manager', 'managers_count': managers_count}
    return render(request, 'manager_list.html', context)

@login_required(login_url='sign_in')
def delete_manager(request, id):
    manager = Manager.objects.get(id=id)
    if request.method == 'POST':
        manager.delete()
        messages.success(request, 'Manager deleted successfully!')
        # log user activity
        activity = f'{request.user.username} ==> {manager.email}.'
        ActivityLog.objects.create(activity=activity, user=request.user, message='Deleted manager')        
        return redirect(reverse('manager_list'))
    context = {'manager': manager}
    return render(request, 'delete_manager.html', context)



#######
@login_required(login_url='sign_in')
def leave_list(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave added successfully!')
            # log user activity
            activity = f"{request.user.username} ==> {form.cleaned_data.get('employee')}."
            ActivityLog.objects.create(activity=activity, user=request.user, message='Added leave')
            return redirect(reverse('leave_list'))
        else:            
            # Form is not valid, extract specific errors and return an error message
            error_msg = 'Leave form contains errors. Please correct them and try again.'
            for field, errors in form.errors.items():
                error_msg += f' {field}: {", ".join(errors)}'
            messages.error(request, error_msg)
            
    form = LeaveForm()
    leaves = Leave.objects.all()
    context = {'leaves': leaves, 'form': form, 'active_page': 'leave'}
    return render(request, 'leave_list.html', context)

@login_required(login_url='sign_in')
def delete_leave(request, id):
    leave = Leave.objects.get(id=id)
    if request.method == 'POST':
        leave.delete()
        messages.success(request, 'Leave deleted successfully!')
        # log user activity
        activity = f'{request.user.username} ==> {leave.employee}.'
        ActivityLog.objects.create(activity=activity, user=request.user, message='Deleted leave')        
        return redirect(reverse('leave_list'))
    context = {'leave': leave}
    return render(request, 'delete_leave.html', context)



#######
@login_required(login_url='sign_in')
def performance_list(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Performance added successfully!')
            # log user activity
            activity = f"{request.user.username} ==> {form.cleaned_data.get('employee')}."
            ActivityLog.objects.create(activity=activity, user=request.user, message='Added performance')
            return redirect(reverse('performance_list'))
        else:            
            # Form is not valid, extract specific errors and return an error message
            error_msg = 'Performance form contains errors. Please correct them and try again.'
            for field, errors in form.errors.items():
                error_msg += f' {field}: {", ".join(errors)}'
            messages.error(request, error_msg)
            
    form = PerformanceForm()
    performances = Performance.objects.all()
    performances_total = performances.count()
    context = {'performances': performances, 'form': form, 'active_page': 'performance', 'performances_total': performances_total}
    return render(request, 'performance_list.html', context)

@login_required(login_url='sign_in')
def delete_performance(request, id):
    performance = Performance.objects.get(id=id)
    if request.method == 'POST':
        performance.delete()
        messages.success(request, 'Performance deleted successfully!')
        # log user activity
        activity = f'{request.user.username} ==> {performance.employee}.'
        ActivityLog.objects.create(activity=activity, user=request.user, message='Deleted performance')
        return redirect(reverse('performance_list'))
    context = {'performance': performance}
    return render(request, 'delete_performance.html', context)





##########
@login_required(login_url='sign_in')
def salary_list(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salary added successfully!')
            # log user activity
            activity = f"{request.user.username} ==> {form.cleaned_data.get('salary_amount')}."
            ActivityLog.objects.create(activity=activity, user=request.user, message='Added salary')
            return redirect(reverse('salary_list'))
        else:            
            # Form is not valid, extract specific errors and return an error message
            error_msg = 'Salary form contains errors. Please correct them and try again.'
            for field, errors in form.errors.items():
                error_msg += f' {field}: {", ".join(errors)}'
            messages.error(request, error_msg)
    form = SalaryForm()
    salaries = Salary.objects.all()
    context = {'salaries': salaries, 'form': form, 'active_page': 'salary'}
    return render(request, 'salary_list.html', context)

@login_required(login_url='sign_in')
def delete_salary(request, id):
    salary = Salary.objects.get(id=id)
    if request.method == 'POST':
        salary.delete()
        messages.success(request, 'Salary deleted successfully!')
        # log user activity
        activity = f'{request.user.username} ==> {salary.salary_amount}.'
        ActivityLog.objects.create(activity=activity, user=request.user, message='Deleted salary')
        return redirect(reverse('salary_list'))
    context = {'salary': salary, }
    return render(request, 'delete_salary.html', context)



#######
@login_required(login_url='sign_in')
def training_list(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Training added successfully!')
            # log user activity
            activity = f"{request.user.username} ==> {form.cleaned_data.get('employee')}."
            ActivityLog.objects.create(activity=activity, user=request.user, message='Added training')
            return redirect(reverse('training_list'))
    form = TrainingForm()
    trainings = Training.objects.all()
    context = {'trainings': trainings, 'form': form, 'active_page': 'training'}
    return render(request, 'training_list.html', context)

@login_required(login_url='sign_in')
def delete_training(request, id):
    training = Training.objects.get(id=id)
    if request.method == 'POST':
        training.delete()
        messages.success(request, 'Training deleted successfully!')
        # log user activity
        activity = f'{request.user.username} ==> {training.employee}.'
        ActivityLog.objects.create(activity=activity, user=request.user, message='Deleted training')
        return redirect(reverse('training_list'))
    context = {'training': training}
    return render(request, 'delete_training.html', context)





###
@login_required(login_url='sign_in')
def job_list(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job added successfully!')
            # log user activity
            activity = f"{request.user.username} ==> {form.cleaned_data.get('title')}."
            ActivityLog.objects.create(activity=activity, user=request.user, message='Added job')
            return redirect(reverse('job_list'))
        else:
            # Form is not valid, extract specific errors and return an error message
            error_msg = 'Job form contains errors. Please correct them and try again.'
            for field, errors in form.errors.items():
                error_msg += f' {field}: {", ".join(errors)}'
            messages.error(request, error_msg)
    form = JobForm()
    jobs = Job.objects.all()
    context = {'jobs': jobs, 'form': form, 'active_page': 'job'}
    return render(request, 'job_list.html', context)

@login_required(login_url='sign_in')
def delete_job(request, id):
    job = Job.objects.get(id=id)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        # log user activity
        activity = f'{request.user.username} ==> {job.title}.'
        ActivityLog.objects.create(activity=activity, user=request.user, message='Deleted job')
        return redirect(reverse('job_list'))
    context = {'job': job}
    return render(request, 'delete_job.html', context)



#####
@login_required(login_url='sign_in')
def recruitment_list(request):
    if request.method == 'POST':
        form = RecruitmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recruitment added successfully!')
            return redirect(reverse('recruitment_list'))
    form = RecruitmentForm()
    recruitments = Recruitment.objects.all()
    context = {'recruitments': recruitments, 'form': form, 'active_page': 'recruitment'}
    return render(request, 'recruitment_list.html', context)

@login_required(login_url='sign_in')
def delete_recruitment(request, id):
    recruitment = Recruitment.objects.get(id=id)
    if request.method == 'POST':
        recruitment.delete()
        messages.success(request, 'Recruitment deleted successfully!')
        return redirect(reverse('recruitment_list'))
    context = {'recruitment': recruitment}
    return render(request, 'delete_recruitment.html', context)

@login_required(login_url='sign_in')
def activity_log(request):    
    activities = ActivityLog.objects.all()
    context = {'activities': activities,'active_page': 'activities'}
    return render(request, 'activities.html', context)
