
from django import forms
from .models import Customer


class PayForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ("active", "book_date")
        widgets = {
            "room_id": forms.HiddenInput(),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "city":forms.TextInput(attrs={"class":"form-control"}),
            "phone_number":forms.TextInput(attrs={"class":"form-control"}),
            "id_number":forms.TextInput(attrs={"class":"form-control"}),


        }

    # first_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # city = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone_number = forms.CharField(max_length=16,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # id_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))

        
