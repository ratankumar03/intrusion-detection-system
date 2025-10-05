from django.db import models
# sniffer/models.py
# from django.db import models

class CapturedPacket(models.Model):
    source_ip = models.CharField(max_length=100)
    destination_ip = models.CharField(max_length=100)
    protocol = models.CharField(max_length=50)
    length = models.IntegerField()
    payload = models.TextField()

    def __str__(self):
        return f"{self.source_ip} -> {self.destination_ip}"

# Create your models here.
