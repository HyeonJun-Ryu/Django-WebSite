from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50)
    images = models.ImageField(blank=True, upload_to="images", null=True)
    contents = models.TextField()

    def __str__(self):
        return self.postname