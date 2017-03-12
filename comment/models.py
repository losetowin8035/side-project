from __future__ import unicode_literals

from django.db import models

from core.models import CreateUpdateBaseModel


class Comment(CreateUpdateBaseModel):
    display_name = models.CharField(max_length=30)
    article_id = models.IntegerField()
    content = models.TextField()
    is_public = models.BinaryField(default=True)
    parrent = models.IntegerField

    class Meta:
        db_table = 'comment'


