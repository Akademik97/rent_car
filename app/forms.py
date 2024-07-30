from django import forms
from .models import RequestToCallBack


class RequestToCallBackForm(forms.ModelForm):
    class Meta:
        model = RequestToCallBack
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше ім'я"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваш телефон"}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Ваше повідомлення", 'rows': 4}),
        }
