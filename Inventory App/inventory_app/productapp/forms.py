from django import forms

from productapp.models import product


class productform(forms.ModelForm): # HTML widgets
                                # validations

    class Meta: # data/info configuration details for the class
       model = product
       #fields = '__all__'
       #fields = ('name' , 'description', 'count', 'location')
       exclude = ('date_added',)