from django.db import models

# Create your models here.
class video_link(models.Model):
    link = models.URLField()
    content = models.CharField(max_length=900)
    video_contents = models.JSONField(null=True)

    def __str__(self):
        return self.content

# class Video_comments(models.Model):
#     video_id = models.ForeignKey(video_link, on_delete=models.CASCADE)
#     comment_csv =