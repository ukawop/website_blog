from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ["create_at"]
        labels = {
            "name": "Имя",
            "email": "Электронная почта",
            "website": "Мессенджер",
            "message": "Ваше сообщение",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Мария'}),
            'email': forms.EmailInput(attrs={'placeholder': 'mariaq123@mail.ru'}),
            'website': forms.TextInput(attrs={'placeholder': 'Не обязательно(+79777772222 / https://vk.com/maria_q123)'}),
            'message': forms.Textarea(attrs={'placeholder': 'Текст'})
        }