from django import forms 
from .models import employee 


class employeeForm(forms.ModelForm) : 
    class Meta : 
        model = employee  
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        lables = {
            'fullname' : 'Full name', 
            'emp_code' : 'Emp. Code'
        }
    def __init__(self, *args, **kwargs):
        super(employeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
