from django import forms
from .models import Review, Product


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())

    class Meta(object):
        model = Review
        fields = ['text', 'product']
        #exclude = ('id', 'product')
