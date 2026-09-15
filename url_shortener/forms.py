from django import forms


class UrlForm(forms.Form):

    link = forms.URLField(
        max_length=1000,
        label="URL"
    )

    alias = forms.CharField(
        max_length=50,
        label="Custom Alias"
    )