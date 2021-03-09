from django.db import models

# Create your models here.

class Warden(models.Model):

    Gender = ['MALE', 'FEMALE', 'OTHER']
    Department = ['CS', 'IT', 'ECE', 'EEE', 'ME', 'CV', 'MT', 'CH']

    warden_id    : models.IntegerFiled(primary_key = True)
    name         : models.CharField(max_length = 200)
    password     : models.CharField(max_length = 200)
    department   : models.CharField(choices = Department)
    email        : models.EmailField(max_length = 200)
    contact      : models.CharField(max_length = 20)
    gender       : models.CharField(choices = Gender)
    
class Complaint:
    Students      : models.ForiegnKey(Students, on_delete = models.Cascade)
    complaint    : models.TextField()
    create_date : models.DateField(auto_now_add = True)
    update_date : models.DateField(auto_now = True)

class Building:

    choices_block = ['GH1', 'GH2', 'GH3', 'GH4', 'BH1', 'BH2', 'BH3', 'BH4']
    choices_no_of_floor = [0,1,2,3]

    type_block   : models.CharFiled(primary_key = True, choices = choices_block)
    num_of_floors : models.IntegerFiled(choice = choices_no_of_floor)
    rooms_per_floor : models.PositiveSmallIntegerField()
