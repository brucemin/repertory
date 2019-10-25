from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class commodity(models.Model):
    name = models.CharField(max_length=32)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    prict = models.FloatField()
    describe = models.CharField(max_length=32)

class auction(models.Model):
    stop = models.CharField(max_length=32)
    a_price = models.FloatField()
    u_id = models.ForeignKey(to="User",to_field="id",on_delete=models.CASCADE)
    u_name = models.CharField(max_length=32)
    c_id  = models.ForeignKey(to="commodity",to_field="id",on_delete=models.CASCADE)


