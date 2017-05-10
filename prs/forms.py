from django import forms
from geoposition import Geoposition
from geoposition.fields import GeopositionField

class UserForm(forms.Form):
    genderchoices = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    email = forms.CharField(max_length=50)
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=20)
    gender = forms.ChoiceField(choices=genderchoices, required=True)

class ReportForm(forms.Form):
    vectors = (
        ('aedes', 'Aedes Mosquito'),
        ('rat', 'Rat'),
    )

    amount = (
        ('5', '1 - 10'),
        ('18', '11 - 25'),
        ('38', '26 - 50'),
        ('75', '51 - 100'),
    )
    Vector = forms.ChoiceField(choices=vectors, required=True)
    Vector_Number = forms.ChoiceField(choices=amount, required=True)
    Latitude = forms.DecimalField(max_digits=25, decimal_places=20, required=True)
    Longitude = forms.DecimalField(max_digits=25, decimal_places=20, required=True)
    #case_date = forms.DateTimeField
