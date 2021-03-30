from django.contrib import admin
from .models import Student, Warden, Building, Complaint, GH1, GH2, GH3, GH4, BH1, BH2, BH3, BH4, WaitingTable,room_Allocation
# Register your models here.


# Register your models here.
from django.contrib.auth.admin import UserAdmin

from hostel_management.models import CustomUser


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)

admin.site.register(Student)
admin.site.register(Building)
admin.site.register(Warden)
admin.site.register(GH1)
admin.site.register(GH2)
admin.site.register(GH3)
admin.site.register(GH4)
admin.site.register(BH1)
admin.site.register(BH2)
admin.site.register(BH3)
admin.site.register(BH4)
admin.site.register(Complaint)
admin.site.register(WaitingTable)
admin.site.register(room_Allocation)