from django import forms
from .models import Post

class PostForm(forms.ModelForm):  # ModelFormの一種だと伝えている

    class Meta:
        model = Post   # フォーム作成に使うモデルを伝えている
        fields = ('title', 'text',)  # フィールドに置くものの指定