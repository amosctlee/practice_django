from django.forms import ModelForm
from .models import Article


class ArticleModelForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'active']
