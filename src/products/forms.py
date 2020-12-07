from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={"placeholder": "your title holder"}
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "your descriptions",
            "class": "new-class-name two",
            "id": "my-id-for-textareas",
            "rows": 3,
            "cols": 5
        }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("this is not a valid title....")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={"placeholder": "your title holder"}
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "your descriptions",
            "class": "new-class-name two",
            "id": "my-id-for-textareas",
            "rows": 3,
            "cols": 5
        }))
    price = forms.DecimalField(initial=199.99)
