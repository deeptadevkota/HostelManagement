from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_data = ((1, "Warden"), (2, "Student"))
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=10)


class Student(models.Model):
    roll_no = models.CharField(primary_key=True, max_length=200)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    year = models.IntegerField(default=2019)
    branch = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)


class Warden(models.Model):
    warden_id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    gender = models.CharField(max_length=200)



class Building(models.Model):
    type_block = models.CharField(primary_key=True, max_length=200)
    num_of_floors = models.IntegerField()
    rooms_per_floor = models.IntegerField()
    block_name = models.OneToOneField(Warden,
                                      on_delete=models.CASCADE, default=None)


class Block(models.Model):
    block_name = models.ForeignKey(
        Building, on_delete=models.CASCADE, null=True, default=None, related_name='block_name_building')
    room_no = models.CharField(max_length=50)
    roll_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, default=None, related_name='roll_1_student')
    roll_2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, default=None, related_name='roll_2_student')
    roll_3 = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, default=None, related_name='roll_3_student')

    class Meta:
        unique_together = (("block_name", "room_no"),)


class Complaint(models.Model):
    complaint_id = models.IntegerField(primary_key=True)
    Students = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, default=None)
    complaint = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Warden.objects.create(admin=instance)
        if instance.user_type==2:
            Student.objects.create(admin=instance)
       
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.warden.save()
    if instance.user_type==2:
        instance.student.save()



