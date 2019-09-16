# Generated by Django 2.2.5 on 2019-09-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0008_auto_20190909_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='things',
            name='date_of_completion',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='things',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in_process', 'In process'), ('done', 'Done')], default='new', max_length=40),
        ),
    ]
