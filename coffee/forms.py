from django import forms

from coffee.variables.ModelsConstants import MAX_LENGTH_USER_NAME


class GiftTo(forms.Form):
    giftTo = forms.CharField(max_length=MAX_LENGTH_USER_NAME)
