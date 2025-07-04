# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Skill
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Existing email.")
        return email
    


EXPERIENCE_LEVELS = [
    ('JR', 'Junior'),
    ('MD', 'Mid'),
    ('SR', 'Senior'),
    ('EX', 'Experto'),
]
class CustomUserChangeForm(UserChangeForm):
    password = None
    username = forms.CharField(disabled=True)

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'w-full px-4 py-2 rounded bg-[#1C114A] text-white',
            'size': '6'
        }),
        required=False
    )

    level = forms.ChoiceField(
        choices=EXPERIENCE_LEVELS,
        widget=forms.RadioSelect,
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio','level', 'github', 'linkedin', 'twitter', 'discord']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            self.fields.pop('password')

