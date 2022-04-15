from .models import Resume
from django import forms

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

JOB_CITY_CHOICES = [
    ('Delhi', 'Delhi'),
    ('Gurugram', 'Gurugram'),
    ('Noida', 'Noida'),
    ('Banglore', 'Banglore'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(choices=JOB_CITY_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name', 'dob', 'email', 'gender', 'profile_image', 'mobile', 'locality', 'city', 'pin', 'state', 'job_city', 'file']
        labels = {'name':'Full Name', 'dob':'Date of Birth', 'profile_image':'Image', 'pin':'Pin code', 'job_city':'Prefered Job Location', 'file':'Resume'}
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }