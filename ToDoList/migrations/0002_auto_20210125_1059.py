# Generated by Django 3.1.5 on 2021-01-25 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='ToDoList.category'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
