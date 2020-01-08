from django import forms


class Login(forms.Form):
    name = forms.CharField(label="Enter your Name")
    email = forms.EmailField(label="Enter your Email address")
    text = forms.CharField(widget=forms.Textarea)
