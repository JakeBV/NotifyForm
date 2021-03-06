from django.db import models


class Post(models.Model):
    tokens_devices = models.TextField()
    notification_title = models.CharField(max_length=62)
    notification_body = models.TextField(max_length=2000)
    payload_title = models.CharField(max_length=100)
    payload_body = models.TextField(max_length=1900)

    def publish(self):
        self.save()
