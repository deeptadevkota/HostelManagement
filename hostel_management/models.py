from django.db import models

# Create your models here.


class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    year = models.IntegerField()
    branch = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

class Building(models.Model):
    block_name = models.CharField(primary_key = True, max_length = 50 ,default=None)
    num_of_floors = models.IntegerField()
    rooms_per_floor = models.IntegerField()


class GH1(models.Model):
    room_no = models.IntegerField(primary_key = True)
    roll_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_1_student_GH1')
    roll_2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_2_student_GH1')
    roll_3 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_3_student_GH1')

class GH2(models.Model):
    room_no = models.IntegerField(primary_key = True)
    roll_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_1_student_GH2')
    roll_2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_2_student_GH2')

class GH3(models.Model):
    room_no = models.IntegerField(primary_key = True)
    roll_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_1_student_GH3')

class GH4(models.Model):
    room_no = models.IntegerField(primary_key = True)
    roll_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_1_student_GH4')

class BH1(models.Model):
    room_no = models.IntegerField(primary_key = True)
    roll_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_1_student_BH1')
    roll_2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_2_student_BH1')
    roll_3 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_3_student_BH1')

class BH2(models.Model):
    room_no = models.IntegerField(primary_key = True)
    roll_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_1_student_BH2')
    roll_2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_2_student_BH2')

class BH3(models.Model):
    room_no = models.IntegerField(primary_key = True)
    roll_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_1_student_BH3')

class BH4(models.Model):
    room_no = models.IntegerField(primary_key = True)
    roll_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, default=None, related_name='roll_1_student_BH4')



class Warden(models.Model):
    warden_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=20)
    gender = models.CharField(max_length=200)
    block_name = models.ForeignKey(Building,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Complaint(models.Model):
    complaint_id = models.IntegerField(primary_key=True)
    Students = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, default=None)
    complaint = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)