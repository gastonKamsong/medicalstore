from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={
            'class': 'border border-gray-300 rounded px-3 py-2 focus:ring-2 focus:ring-medical-blue focus:border-transparent'
        })
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

class CartUpdateWeightForm(forms.Form):
    weight = forms.IntegerField(min_value=10)