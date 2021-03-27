# Generated by Django 3.1.7 on 2021-03-26 06:18

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
            name='CustomUser',
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
                ('user_type', models.CharField(choices=[(2, 'Warden'), (3, 'Student')], default=1, max_length=20)),
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
            name='BH1',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('roll_2', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('roll_3', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BH2',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('roll_2', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BH3',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BH4',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('block_name', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('num_of_floors', models.IntegerField()),
                ('rooms_per_floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GH1',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('roll_2', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('roll_3', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GH2',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('roll_2', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GH3',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GH4',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaitingTable',
            fields=[
                ('roll_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Warden',
            fields=[
                ('warden_id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=200)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('block_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.building')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=2019)),
                ('branch', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=20)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.IntegerField(primary_key=True, serialize=False)),
                ('complaint', models.TextField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('Students', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='hostel_management.student')),
            ],
        ),
    ]
