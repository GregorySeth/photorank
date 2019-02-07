from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default = 1)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE) #user that uploads new photo

    def prettify_date(self):
        return self.pub_date.strftime('%d.%m.%Y')

    def body(self):
        return self.summary[:100]

    def __str__(self):
        return self.title
