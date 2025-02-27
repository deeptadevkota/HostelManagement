from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_data = ((2, "Warden"), (3, "Student"))
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=20)


class Student(models.Model):
    roll_no = models.CharField(max_length=200)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    year = models.IntegerField(default=2019)
    branch = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.roll_no


class Building(models.Model):
    block_name = models.CharField(
        primary_key=True, max_length=50, default=None)
    num_of_floors = models.IntegerField()
    rooms_per_floor = models.IntegerField()

    def __str__(self):
        return self.block_name


class Warden(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    gender = models.CharField(max_length=200)
    block_name = models.ForeignKey(
        Building, on_delete=models.CASCADE, default=None, null=True)


class GH1(models.Model):
    room_no = models.IntegerField(primary_key=True)
    roll_1 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)
    roll_2 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)
    roll_3 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)


class GH2(models.Model):
    room_no = models.IntegerField(primary_key=True)
    roll_1 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)
    roll_2 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)


class GH3(models.Model):
    room_no = models.IntegerField(primary_key=True)
    roll_1 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)


class GH4(models.Model):
    room_no = models.IntegerField(primary_key=True)
    roll_1 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)


class BH1(models.Model):
    room_no = models.IntegerField(primary_key=True)
    roll_1 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)
    roll_2 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)
    roll_3 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)


class BH2(models.Model):
    room_no = models.IntegerField(primary_key=True)
    roll_1 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)
    roll_2 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)


class BH3(models.Model):
    room_no = models.IntegerField(primary_key=True)
    roll_1 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)


class BH4(models.Model):
    room_no = models.IntegerField(primary_key=True)
    roll_1 = models.CharField(null=True, blank=True,
                              default=None, max_length=10)


class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    roll_no = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, default=None)
    complaintText = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)


class WaitingTable(models.Model):
    roll_no = models.CharField(primary_key=True, max_length=10)
    gender = models.CharField(max_length=50)


class room_Allocation(models.Model):
    is_room_allocation_set = models.IntegerField(default=1)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 2:
            Warden.objects.create(admin=instance)
        if instance.user_type == 3:
            Student.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 2:
        instance.warden.save()
    if instance.user_type == 3:
        instance.student.save()
