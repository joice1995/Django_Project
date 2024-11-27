from django import forms   
from .models import Booked

class date(forms.DateInput):
    input_type="date"

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booked
        fields = "__all__"
        
        widgets = {
            'booking_date' : date
        }
        
        
        labels={
            'pat_name' : "Name : ",
            'pat_number' : "phone number",
            'pat_email' : "enter your email id",
            'doc_name' : "doctor name",
            'booking_date' : "Booking Date "
            
        }
