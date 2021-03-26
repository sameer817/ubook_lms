# Generated by Django 3.1.7 on 2021-03-17 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '0004_auto_20210317_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classhistory',
            name='designation',
        ),
        migrations.AddField(
            model_name='classes',
            name='assis_professor',
            field=models.ForeignKey(limit_choices_to={'type': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assis', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classes',
            name='depart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
        ),
        migrations.AddField(
            model_name='classhistory',
            name='assis_professor',
            field=models.ForeignKey(limit_choices_to={'type': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ass', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classhistory',
            name='professor',
            field=models.ForeignKey(limit_choices_to={'type': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
