from django import forms

class TranslationForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Text to Translate', required=True)
    language = forms.ChoiceField(choices=[
        ('hi', 'Hindi'),
        ('de', 'German'),
        ('fr', 'French'),
        ('it', 'Italian'),
    ], label='Select Language')
