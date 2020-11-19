from django.db import models
from django.core import validators
from django.core.validators import RegexValidator


class Item(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'テスト'),
    )

    NAME_CHOICES = (
        ('高橋悠人', '高橋悠人'),
        ('足立雄介', '足立雄介'),
        ('井上貴子', '井上貴子'),
        ('柿崎義弘', '柿崎義弘'),
        ('斎藤祐樹', '斎藤祐樹'),
        ('和田昭雄', '和田昭雄'),
    )

    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric are allowed.')

    name = models.CharField(
        verbose_name='名前',
        choices=NAME_CHOICES,
        max_length=20,
    )

    takuhaikenpin = models.IntegerField(
        verbose_name='宅配検品',
        validators=[numeric],
        #blank=True,
        null=True,
        default=0
    )

    sonotakenpin = models.IntegerField(
        verbose_name='その他検品',
        validators=[numeric],
        # blank=True,
        null=True,
        default=0
    )

    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'