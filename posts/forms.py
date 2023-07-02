from django import forms
from .models import Post
from .validators import validate_symbols
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]  #'__all__'

    # Form에서 유효성 검사하기 1. clean_data  2. formfield 사용하기
    def clean_title(self):
        title = self.cleaned_data["title"]
        if "*" in title:
            raise ValidationError("*은 포함될 수 없습니다.")
        return title
