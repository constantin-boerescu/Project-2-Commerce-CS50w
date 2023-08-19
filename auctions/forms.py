from django import forms

class CreateForm(forms.Form):
    title = forms.CharField(
        label='Title', 
        max_length=100,
        required=True, 
        widget=forms.TextInput(attrs={'class':'auct_title', 'placehoder':'Title'}))
    
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class':'text_area', 'placehoder':'Description'}))

    img_url = forms.CharField(
        label='Image Url', 
        max_length=2048,
        required=False, 
        widget=forms.TextInput(attrs={'class':'auct_title', 'placehoder':'Image url'}))
    
    price = forms.DecimalField(
        label='Price',
        required=False,
        initial=0.00,
        widget=forms.NumberInput(attrs={
            'class': 'auct_title',
            'placeholder': 'Estimated price',
            'min': '0.1',
            'max': '999999999.99',
            'step': '0.1'
        }))
    
    start_bid = forms.DecimalField(
        label='start_bid',
        required=False,
        initial=0.00,
        widget=forms.NumberInput(attrs={
            'class': 'auct_title',
            'placeholder': 'start_bid price',
            'min': '0.1',
            'max': '999999999.99',
            'step': '0.1'
        }))
    
    category = forms.CharField(
        label='Category', 
        max_length=100,
        required=True, 
        widget=forms.TextInput(attrs={'class':'auct_title', 'placehoder':'Category'}))