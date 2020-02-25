from django import forms
import re
from user.models import CustomerUser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForms(forms.Form):
    username = forms.CharField(label = 'User', max_length=30)
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label= 'Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label= 'Enter the password', widget=forms.PasswordInput())
    address = forms.CharField(max_length=255, label= 'Address')
    phone_number = forms.CharField(max_length=15, label='Phone number')
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Invalid password")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản chứa kí tự đặc biệt")

        try:
            CustomerUser.objects.get(username= username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tên tài khoản đã tồn tại")


    def save(self):
        CustomerUser.objects.create_user(username=self.cleaned_data['username'], email= self.cleaned_data['email'], password = self.cleaned_data['password1'], address = self.cleaned_data['address'], phone_number = self.cleaned_data['phone_number'])
