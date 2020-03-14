from django import forms 
from home.models import user 
from home.models import appointment
class formUser(forms.ModelForm) : 
    name = forms.CharField(label="Your name", max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm = forms.CharField(widget=forms.PasswordInput())
    class Meta : 
        model = user
        fields = ['name', 'email','password']
 

class formCustomer(forms.ModelForm) : 
    name = forms.CharField(label='Your name', max_length=200)
    service = forms.CharField(label='Service',max_length=200)
    barder = forms.CharField(label='barder',max_length=200)
    email = forms.EmailField(label='email',max_length=200)
    date = forms.CharField(label='date',max_length=200)
    time = forms.CharField(label='time',max_length=200)

    class Meta : 
        model = appointment 
        fields = ['name', 'service', 'email', 'barder', 'date', 'time']

# class formCustomer(forms.ModelForm):
#     class Meta:
#         model = appointment
#         fields = ('name', 'service', 'email', 'barder', 'date', 'time')
#         labels = {
#             'name':'Full Name',
#             'email':'Email'
#         }

    # def __init__(self, *args, **kwargs):
    #     super(appointment,self).__init__(*args, **kwargs)
    #     self.fields['email'].empty_label = "Select"
    #     self.fields['time'].required = False
