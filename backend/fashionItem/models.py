from django.db import models
from colorfield.fields import ColorField


class Category(models.Model):
    category_name = models.CharField('カテゴリー名',max_length=255)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="カテゴリー")
    sub_category_name = models.CharField('サブカテゴリー名',max_length=255)
    def __str__(self):
        return self.sub_category_name

class Item(models.Model):
    sub_category = models.ManyToManyField(SubCategory,verbose_name="サブカテゴリー")
    itemname = models.CharField('商品名',max_length=255)
    price = models.IntegerField('価格',default=0)
    image = models.ImageField(upload_to="images", verbose_name="画像", null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.itemname

class ItemDetail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, verbose_name="アイテム")
    color = ColorField("色",default="#f4be9b")
    itemcount = models.IntegerField("商品数",default=0)
    note = models.TextField("詳細説明")

    def __str__(self):
        return self.item.itemname
