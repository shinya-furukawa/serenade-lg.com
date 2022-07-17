from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('Email',max_length=255, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username

class Address(models.Model):
    zipcode = models.CharField('郵便番号', max_length=20)
    address = models.CharField('住所', max_length=255)
    building = models.CharField('建物名',max_length=255)

    def __str__(self):
        return self.building


class Customer(models.Model):
    username = models.CharField('ユーザー名' , max_length=255)
    email = models.EmailField('メールアドレス' , max_length=255, unique=True)
    password = models.CharField('パスワード', max_length=255)
    phone = models.CharField('電話番号' , max_length=20, null=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, verbose_name="住所")
    age = models.IntegerField('年齢',null=True)
    gender = models.SmallIntegerField('性別', choices=[(0,"その他"),(1,"女性"),(2,"男性")], default=0)
    is_acrive = models.BooleanField('有効',default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username

