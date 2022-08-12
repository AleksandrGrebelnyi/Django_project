from django import forms
from .models import UserReservation


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Ваше имя',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
        })
    )
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'name': 'email',
        'id': 'email',
        'placeholder': 'Ваш Email (имэйл)',
        'data-rule': 'email',
        'data-msg': 'Please enter a valid email',

    }))

    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'phone',
        'id': 'phone',
        'placeholder': 'Ваш телефон',
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars',
    }))

    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'class': 'form-control',
        'name': 'people',
        'id': 'people',
        'placeholder': 'Количество людей',
        'data-rule': 'minlen:1',
        'data-msg': 'Please enter at least 1 chars',
    }))

    message = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        'type': 'number',
        'class': 'form-control',
        'name': 'message',
        'rows': '5',
        'placeholder': 'Сообщение',
        'required': 'required',
    }))

    class Meta:
        model = UserReservation
        fields = ('name', 'email', 'phone', 'persons', 'message', )