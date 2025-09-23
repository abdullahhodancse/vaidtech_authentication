from django.db import models
from app1.models.custome_user import  User


class patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    age=models.IntegerField()
    disease=models.CharField(max_length=60)

    def __str__(self):
        return f"{self.user.first_name}-{self.user.last_name}"