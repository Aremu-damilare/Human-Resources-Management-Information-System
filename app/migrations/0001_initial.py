# Generated by Django 4.2 on 2023-04-21 00:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Female', max_length=10)),
                ('nationality', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('employment_date', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('date_posted', models.DateField(null=True)),
                ('closing_date', models.DateField(null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_date', models.DateField()),
                ('training_location', models.CharField(max_length=200)),
                ('training_duration', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
                ('training_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trainingtype')),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('recruitment_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_posted', models.DateField()),
                ('closing_date', models.DateField()),
                ('job_description', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.position')),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance_date', models.DateField()),
                ('performance_score', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
                ('performance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.performancetype')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('contact_number', models.CharField(max_length=15, null=True)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.job')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('approval_status', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
                ('leave_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.leavetype')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='employment_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employmentstatus'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.job'),
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.manager'),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.salary'),
        ),
    ]
