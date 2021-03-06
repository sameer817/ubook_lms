# Generated by Django 3.1.7 on 2021-03-21 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0005_auto_20210317_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='class_year',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='depart',
            field=models.ForeignKey(limit_choices_to={'status': 3}, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
        ),
    ]
