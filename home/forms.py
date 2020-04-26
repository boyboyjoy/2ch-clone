from django import forms
class UploadForm(forms.Form):
    image=forms.ImageField(label='Add picture')
    name=forms.CharField(label='Text')

