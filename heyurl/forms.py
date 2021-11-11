from django import forms

from heyurl.models import Url


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('original_url', )

    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields['original_url'].widget.attrs['class'] = 'form-control'
        self.fields['original_url'].widget.attrs['placeholder'] = 'http://www.example.com'
