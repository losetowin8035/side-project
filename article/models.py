from __future__ import unicode_literals

from django.db import models

from core.models import CreateUpdateBaseModel


class Article(CreateUpdateBaseModel):
    title = models.CharField(max_length=80)
    desc = models.CharField(max_length=170)
    slug = models.SlugField()
    content = models.TextField()
    branch_id = models.PositiveSmallIntegerField(default=0)
    thumb_img = models.IntegerField(default=0)
    num_comment = models.PositiveSmallIntegerField(default=0)
    num_hit = models.BigIntegerField(default=0)
    allow_comment = models.BinaryField(default=True)
    is_public = models.BinaryField(default=True)

    class Meta:
        db_table = 'article'

