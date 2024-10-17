from django import forms
from .models import UserProfile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError 

class RegistroForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")
    type_document = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES, required=True, label="Tipo de documento")
    number_document = forms.CharField(max_length=20, required=True, label="Número de documento")
    phone = forms.CharField(required=True, label="Teléfono", widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmarscontraseña")

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'type_document', 'number_document', 'phone', 'password']

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserProfile.objects.filter(email=email).exists():
            raise ValidationError('El correo electrónico ya está registrado.')
        return email

    def clean_number_document(self):
        number_document = self.cleaned_data.get('number_document')
        if not number_document.isdigit():
            raise ValidationError('El número de documento debe contener solo dígitos.')
        
        if UserProfile.objects.filter(number_document=number_document).exists():
            raise ValidationError('El documento de identidad ya existe')
        return number_document

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise ValidationError('El número de teléfono debe contener solo dígitos.')
        
        if len(phone) != 10:
           raise ValidationError('El número de teléfono debe tener exactamente 10 dígitos.')
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
 

        if password != password_confirm:
            self.add_error('password_confirm', 'Las contraseñas no coinciden.')
           
        return cleaned_data
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"]) 
        if commit:
            user.save()
        return user
