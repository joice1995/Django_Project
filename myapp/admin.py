from django.contrib import admin
from .models import Department, medical, Doctor,Booked

# Register your models here.
admin.site.register(Department)
admin.site.register(medical)
admin.site.register(Doctor)

class Bookingadmin(admin.ModelAdmin):
    list_display = ('id','pat_name','pat_number','pat_email', 'doc_name', 'booking_date', 'booked_on')
admin.site.register(Booked, Bookingadmin)