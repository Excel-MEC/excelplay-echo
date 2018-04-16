from django import forms

class SubmitForm(forms.Form):
	fid = forms.IntegerField()
	files_echo = forms.FileField()