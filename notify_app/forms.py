from django import forms

from .models import Post


class NotifyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('tokens_devices', 'notification_title', 'notification_body', 'payload_title', 'payload_body',)
        widgets = {
            'notification_title': forms.TextInput(attrs={'placeholder': 'Notification title',
                                                         'class': 'styled-input'}),
            'payload_title': forms.TextInput(attrs={'placeholder': 'Payload title', 'class': 'styled-input'}),
            'tokens_devices': forms.Textarea(attrs={'placeholder': 'Tokens devices: token1, token2, token3, etc',
                                                    'class': 'styled-input wide'}),
            'notification_body': forms.Textarea(attrs={'placeholder': 'Notification body',
                                                       'class': 'styled-input wide'}),
            'payload_body': forms.Textarea(attrs={'placeholder': 'Payload body', 'class': 'styled-input wide'}),
        }
        labels = {
            'notification_title': '', 'payload_title': '',
            'tokens_devices': '', 'notification_body': '', 'payload_body': ''
        }
