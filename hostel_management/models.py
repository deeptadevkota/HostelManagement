from django.db import models

# Create your models here.
class Students(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    year = models.IntegerField()
    branch = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

class Blocks(models.Model):
    block_name = models.CharField(max_length=50)
    room_no = models.CharField(max_length=50)
    roll_1 = models.ForeignKey(
        Students, on_delete=models.CASCADE, null=True, default=None, related_name='roll_1_student')
    roll_2 = models.ForeignKey(
        Students, on_delete=models.CASCADE, null=True, default=None, related_name='roll_2_student')
    roll_3 = models.ForeignKey(
        Students, on_delete=models.CASCADE, null=True, default=None, related_name='roll_3_student')