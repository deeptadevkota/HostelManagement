from django.contrib import admin
from .models import Student, Warden, Building, Block, Complaint
# Register your models here.


# Register your models here.
from django.contrib.auth.admin import UserAdmin

from hostel_management.models import CustomUser


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)


admin.site.register(Student)
admin.site.register(Warden)
admin.site.register(Building)
admin.site.register(Block)
admin.site.register(Complaint)