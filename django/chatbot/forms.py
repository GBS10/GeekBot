from django import forms
   
# creating a form 
class InputForm(forms.Form):
    user_name = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput())

class AddWordForm(forms.Form):
    word = forms.CharField(max_length = 100)
    definition = forms.CharField(max_length = 300)