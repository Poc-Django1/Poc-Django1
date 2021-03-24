from django import forms
from .models import subjectdetails
 
class MyForm(forms.ModelForm):
  subject = forms.CharField(label='subject', max_length=30)
  class Meta:
    model = subjectdetails
    fields = ['id', 'subject', ]
    labels = {'id' : 'ID', 'subject' : 'Subject', 'Created' : 'Created_at', 'updated' : 'Updated_at'}
