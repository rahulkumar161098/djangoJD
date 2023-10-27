from django import forms

class CreateLead(forms.Form):
   first_name= forms.CharField()
   last_name= forms.CharField()
   age= forms.IntegerField(min_value=15, max_value=80)