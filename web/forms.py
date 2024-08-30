from django import forms
from .models import ContactForm
from django.contrib.auth.models import User

class ContactFormForm(forms.Form):
	customer_email = forms.EmailField(label="Correo", widget=forms.EmailInput(
		attrs={
			"class": "form-control",
			"placeholder": "xyz@mail.com"
		}
	))
	customer_name = forms.CharField(max_length=64, label="Nombre", widget=forms.TextInput(
		attrs={
			"class": "form-control",
			"placeholder": "john doe"
		}
	))
	message = forms.CharField(label="Mensaje", widget=forms.Textarea(
		attrs={
			"rows": 4,
			"class": "form-control",
			"placeholder": "Escribenos tu experiencia o recomendación"
		}
	))

class ContactFormModelForm(forms.ModelForm):
	class Meta:
		model = ContactForm
		fields = ['customer_email', 'customer_name', 'message']

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get('password')
		password_confirm = cleaned_data.get('password_confirm')

		if password and password_confirm and password != password_confirm:
			raise forms.ValidationError("Las contraseñas mo coinciden")
		
		return cleaned_data