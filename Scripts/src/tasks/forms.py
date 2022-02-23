from django import forms
from .models import Users


class SignupForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=255,help_text="Enter a valid email")
    password1 = forms.CharField(widget = forms.PasswordInput())
    password2 = forms.CharField(widget = forms.PasswordInput())
    
    class Meta:
        model = Users
        fields = ('name', 'email', 'password1', 'password2')
        labels = {
            'name': 'Name',
            'email': 'Email',
            'password1': 'Password',
            'password2':'Confirm password'
        }

        def clean(self):

            # data from the form is fetched using super function
            super(SignupForm, self).clean()

            # extract the username and text field from the data
            username = self.cleaned_data.get('name')
            email = self.cleaned_data.get('email')
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if email and Users.objects.filter(email=email).exclude(username=username).count():
                raise forms.ValidationError(
                    _("This email address is already in use. Please supply a different email address."))
            return email


            # conditions to be met for the username length
            if len(username) < 5:
                self._errors['username'] = self.error_class([
                    'Minimum 5 characters required'])

            if password1 != password2:
                self._errors['password'] = self.error_class([
                    'Passwords dont match'
                ])

            # return any errors if found
            return self.cleaned_data