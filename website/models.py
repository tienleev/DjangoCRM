from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    fist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return(f"{self.fist_name} {self.last_name}")