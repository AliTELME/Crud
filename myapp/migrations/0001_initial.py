# Generated by Django 4.0 on 2022-09-06 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_Name', models.CharField(max_length=100)),
                ('L_Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
    ]
