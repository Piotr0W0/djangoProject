# Generated by Django 3.1.5 on 2021-01-25 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateField(default='2021-01-25')),
                ('deadline_date', models.DateField(default='2021-01-25')),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.DO_NOTHING, to='ToDoList.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
