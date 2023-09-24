from django import forms

class ContactForm(forms.Form):
    '''Contact Form'''
    
    name = forms.CharField(min_length=4, max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'input-field'}))
    email = forms.EmailField(max_length=200, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'input-field'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea-field'}), required=True)
    