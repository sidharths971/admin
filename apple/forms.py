from .models import person,order,comment
from django import forms


class person_form(forms.ModelForm):

    class Meta:
        model = person
        fields = "__all__"


class order_form(forms.ModelForm):

    class Meta:
        model = order
        fields = '__all__'

class comment_form(forms.ModelForm):

    class Meta:
        model = comment
        fields = '__all__'
