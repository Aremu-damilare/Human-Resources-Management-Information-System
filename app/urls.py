from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('employee_department_chart/', views.employee_department_chart, name='employee_department_chart'),
    path('employee_data/', views.employee_data, name='employee_data'),
    
    
    path('staffs/', views.employee_list, name='employee_list'),    
    path('delete-staff/<int:id>/', views.delete_employee, name='delete_employee'),
    
    path('manager/', views.manager_list, name='manager_list'),    
    path('delete-manager/<int:id>/', views.delete_manager, name='delete_manager'),
    
    path('leave/', views.leave_list, name='leave_list'),    
    path('delete-leave/<int:id>/', views.delete_leave, name='delete_leave'),
    
    path('performance/', views.performance_list, name='performance_list'),    
    path('delete-performance/<int:id>/', views.delete_performance, name='delete_performance'),
    
    # ###
    path('salary/', views.salary_list, name='salary_list'),    
    path('delete-salary/<int:id>/', views.delete_salary, name='delete_salary'),
    
    path('training/', views.training_list, name='training_list'),    
    path('delete-training/<int:id>/', views.delete_training, name='delete_training'),
    
    # ###
    path('recruitment/', views.recruitment_list, name='recruitment_list'),    
    path('delete-recruitment/<int:id>/', views.delete_recruitment, name='delete_recruitment'),
    
    path('job/', views.job_list, name='job_list'),    
    path('delete-job/<int:id>/', views.delete_job, name='delete_job'),
    
    
    path('activities/', views.activity_log, name='activities'),
]