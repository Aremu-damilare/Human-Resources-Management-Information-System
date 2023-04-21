# Generated by Django 4.2 on 2023-04-21 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_leave_approval_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruitment',
            name='job_description',
        ),
        migrations.AddField(
            model_name='recruitment',
            name='Job',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.job'),
            preserve_default=False,
        ),
    ]