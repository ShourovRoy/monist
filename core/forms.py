from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_address']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'customer_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Shipping Address', 'rows': 3}),
        }
