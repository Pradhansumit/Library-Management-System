from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


# current directory
from . import models

User = get_user_model()


# creating custom users


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.LMS_USERS
        fields = UserCreationForm.Meta.fields + \
            ("first_name", "last_name", "email", "status")

# updating/changing already exist users


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'status']


# forms to add and update books
class BooksForm(ModelForm):
    class Meta:
        model = models.Books
        fields = [
            "book_name", "book_author", "book_isbn", "book_category",
        ]
