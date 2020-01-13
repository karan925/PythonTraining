from django import forms
from django.core import validators


class Login(forms.Form):
    name = forms.CharField(label="Enter your Name")
    email = forms.EmailField(label="Enter your Email address")
    verify_email = forms.EmailField(max_length=40, label="Verify Email")
    text = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        special_char = ['$', '@', '#', '%']
        check = 0
        if len(password) <= 7:
            raise forms.ValidationError('Password must be 8 or more characters')
        if sum(c.isdigit() for c in password) < 1:
            raise forms.ValidationError('Password must contain one digit')
        if not any(a.isupper() for a in password):
            raise forms.ValidationError('Password must have one uppercase')
        if not any(b.islower() for b in password):
            raise forms.ValidationError('Password must have one lowercase')
        for c in password:
            if c in special_char:
                check += 1
        if check < 2:
            raise forms.ValidationError('Password must contain 2 characters')
        return password


'''validators=[validators.MinLengthValidator(6, "Must be 6 or more characters"),
                                           validators.MaxLengthValidator(10)])'''
