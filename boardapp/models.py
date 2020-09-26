from django.db import models

# Create your models here.
#migrateをしたらadmin.pyに書き込むのを忘れないようにする
#ここの中身はなにか変更するたびにmakemigrationとmigrateする
class BoardModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    auther=models.CharField(max_length=20)
    #ImageFieldは画像を扱うメソッド　中のupload_toはブランクでいい
    #具体的にはsetting.pyでMEDIA_ROOTとMEDIA_URLで設定する
    #これを使うにはpillowというパッケージが必要　sudo pip3でインストールする
    images=models.ImageField(upload_to='')
    #いいねの数
    #null=Trueでnullを許容
    good=models.IntegerField(null=True,blank=True,default=0)
    #既読の人数
    read=models.IntegerField(null=True,blank=True,default=0)
    #既読した人のリスト　同じ人の既読が重複しないように
    readtext=models.CharField(max_length=200,null=True,blank=True,default='')