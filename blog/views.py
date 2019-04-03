from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request): # 下のURLをテンプレート表示するRenderを返す
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # postsにクエリセットを代入
    return render(request, 'blog/post_list.html', {'posts': posts}) # クエリセットを指定

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})