from django import forms
from .models import Developer

class DeveloperForm(forms.ModelForm):

    class Meta:
        model = Developer
        fields = '__all__'
      
    def __init__(self, *args, **kwargs):
        super(DeveloperForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"