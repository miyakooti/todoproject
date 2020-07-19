from django.db import models

# Create your models here.
PRIORITY = (('danger','high'),('info','normal'),('success','low')) #タプル型。右側の値は画面上に表示。左側は内部というイメージ？
class TodoModel(models.Model):
  title = models.CharField(max_length=100) #charは文字に関係、max_engthは必須
  memo = models.TextField() #もしかして、これってカラム？
  priority = models.CharField(
    max_length = 50,
    choices = PRIORITY #選択肢を作る。デフォルトで選択肢の一つを指定しておく。（マイグレーション作成の時に聞かれる）
    )
  duedate = models.DateField()#デフォルトで今日の日付を指定可能
  def __str__(self):
    return self.title #行の名前かな