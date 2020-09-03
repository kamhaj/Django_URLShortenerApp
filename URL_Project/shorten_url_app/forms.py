from django import forms


class URLForm(forms.Form):
    user_url = forms.CharField(label='URL   ',
                               widget=forms.TextInput(attrs={'placeholder':'https://<domain>.com/<parameters>'}))
