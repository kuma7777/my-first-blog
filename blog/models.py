from django.db import models
from django.utils import timezone


class Post(models.Model): # モデル定義(オブジェクト) models.Model=Djangoモデルだという意味
    # プロパティ設定
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 他モデルへのリンク
    title = models.CharField(max_length=200)  # CharField=文字数が制限された(200)テキストを定義するフィールド
    text = models.TextField()                 # 制限なしの長いテキスト用
    created_date = models.DateTimeField(default=timezone.now)  # 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): # ブログを公開する機能
        self.published_date = timezone.now() # 現在時間の取得
        self.save()                          # 保存
    
    def __str__(self): # ポストのタイトルテキストを文字列で返す
        return self.title