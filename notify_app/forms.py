from django import forms

from .models import Post


class NotifyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('tokens_devices', 'title', 'message', 'payload_title', 'payload_body',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '* Title', 'class': 'styled-input'}),
            'payload_title': forms.TextInput(attrs={'placeholder': 'Payload title', 'class': 'styled-input'}),
            'tokens_devices': forms.Textarea(attrs={'placeholder': '* Tokens devices: token1, token2, token3, etc',
                                                    'class': 'styled-input wide'}),
            'message': forms.Textarea(attrs={'placeholder': '* Message', 'class': 'styled-input wide'}),
            'payload_body': forms.Textarea(attrs={'placeholder': 'Payload body', 'class': 'styled-input wide'}),
        }
        labels = {
            'title': '', 'payload_title': '', 'tokens_devices': '', 'message': '', 'payload_body': ''
        }
