from django.contrib.auth import get_user_model
from django.db import models
import datetime
User = get_user_model()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    main_body = models.TextField()
    votes = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.author.username}"


