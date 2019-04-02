from django.shortcuts import render

def post_list(request): # 下のURLをテンプレート表示するRenderを返す
    return render(request, 'blog/post_list.html', {}) 