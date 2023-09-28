from django import forms

class ContactForm(forms.Form):
    '''Contact Form'''
    
    name = forms.CharField(min_length=4, max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'input-field'}))
    email = forms.EmailField(max_length=200, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'input-field'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea-field'}), required=True)


class SearchProjectForm(forms.Form):
    '''Form to search for projects by domain'''
    
    project_domain = [
        ('None', 'Filter by Project Domain'),   
        ('Mobile App Development', 'Mobile App Development'),
        ('Full Stack Web Development', 'Full Stack Web Development'),
        ('Frontend Web Development', 'Frontend Web Development'),
        ('Backend Web Development', 'Backend Web Development'),
        ('Python Development', 'Python Development'),   
        ('Data Science', 'Data Science'),   
    ]
    
    domain = forms.CharField(label=False, required=True, widget=forms.Select(choices=project_domain))
