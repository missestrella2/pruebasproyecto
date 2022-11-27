from django import forms


class IndexForm(forms.Form):

    email = forms.EmailField(required=True)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)