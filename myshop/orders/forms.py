from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        widgets = {
                    'first_name': forms.TextInput(attrs={'class': 'form-input'}),
                    'last_name': forms.TextInput(attrs={'class': 'form-input'}),
                    'email': forms.EmailInput(attrs={'class': 'form-input'}),
                    'address': forms.TextInput(attrs={'class': 'form-input'}),
                    'postal_code': forms.TextInput(attrs={'class': 'form-input'}),
                    'city': forms.TextInput(attrs={'class': 'form-input'}),
                }
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Электронная почта',
            'address': 'Адрес',
            'postal_code': 'Почтовый индекс',
            'city': 'Город',
        }