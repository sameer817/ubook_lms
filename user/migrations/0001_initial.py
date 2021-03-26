# Generated by Django 3.1.7 on 2021-03-15 13:17

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.SmallIntegerField(choices=[(0, 'None'), (1, 'Mmale'), (2, 'Female'), (3, 'Trans')], default=0)),
                ('adhar', models.IntegerField(blank=True, null=True, unique=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('father_name', models.CharField(blank=True, max_length=256, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=256, null=True)),
                ('type', models.IntegerField(choices=[(0, 'None'), (1, 'Student'), (2, 'Staff'), (3, 'lower_staf')], default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_id', models.CharField(max_length=256, unique=True)),
                ('pr_name', models.CharField(max_length=256)),
                ('client', models.CharField(max_length=256)),
                ('start', models.DateField(auto_now_add=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'None'), (1, 'DEV'), (2, ''), (2, 'PROD'), (3, 'LIVE'), (4, 'CLOSED')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.IntegerField(blank=True, null=True)),
                ('addr', models.TextField(blank=True, default='Home')),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('user', models.OneToOneField(limit_choices_to={'type': 1}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.SmallIntegerField(choices=[(0, 'None'), (1, 'PRINCIPLE'), (2, 'HOD'), (2, 'PROFESSOR'), (3, 'ASST-PROFESSOR'), (4, 'ASSOCIAT-PROFESSOR'), (5, 'LAB-INCHARGE'), (6, 'LAB-ASSISTANT')], default=0)),
                ('start', models.DateField(auto_now_add=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.projects')),
                ('user', models.ForeignKey(limit_choices_to={'type': 2}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
