from django.db import models



class mylogin(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    phone=models.CharField(max_length=40)
    class Meta:
        db_table="mylogin"







