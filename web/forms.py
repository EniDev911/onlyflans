from django import forms

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