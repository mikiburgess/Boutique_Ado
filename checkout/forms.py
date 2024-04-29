from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # only show the fields user needs to edit
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, remove auto-generated
            labels, and set autofocus on first field 
        """
        # st up form in usual, default way
        super().__init__(*args, **kwargs)
        # define dictionary of field placeholders to be used in place of form labels
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal code', 
            'town_or_city': 'Town or City', 
            'street_address1': 'Street Address 1', 
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Start on Full Name field when page loads
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # iterate through form fields adding * if required, adding custom placeholder, 
        #  add css for each field, and remove the default labels
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
