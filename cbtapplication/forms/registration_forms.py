from django.forms import ModelForm, CharField
from cbtapplication.models import UserDetail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput


class UserForm(ModelForm):
    username = CharField(max_length=150, required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
    
class UserAdditionalDetailsForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = ['class_year', 'department', 'role', 'is_computer_literate', 'dob']
    