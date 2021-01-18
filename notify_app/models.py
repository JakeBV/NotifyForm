from django.db import models


class Post(models.Model):
    tokens_devices = models.TextField()
    title = models.CharField(max_length=62)
    message = models.TextField(max_length=2000)
    payload_title = models.CharField(max_length=100, blank=True)
    payload_body = models.TextField(max_length=1900, blank=True)

    def publish(self):
        self.save()
