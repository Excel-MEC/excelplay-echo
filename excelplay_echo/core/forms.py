from django import forms


class SubmitForm(forms.Form):
    file_id = forms.IntegerField()
    files_echo = forms.FileField()
