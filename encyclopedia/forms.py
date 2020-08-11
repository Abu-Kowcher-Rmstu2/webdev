from django import forms

class NewTaskForm(forms.Form):
    title = forms.CharField(attrs={'class':'form-control'})
    body = forms.Textarea()
