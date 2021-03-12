from django.contrib import admin
from .models import Student, Warden, Building, Block, Complaint
# Register your models here.


admin.site.register(Student)
admin.site.register(Warden)
admin.site.register(Building)
admin.site.register(Block)
admin.site.register(Complaint)