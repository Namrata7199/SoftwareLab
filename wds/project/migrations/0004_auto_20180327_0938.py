# Generated by Django 2.0.3 on 2018-03-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20180320_1023'),
        ('project', '0003_auto_20180327_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='team_leader',
        ),
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.ManyToManyField(to='index.Profile'),
        ),
    ]
