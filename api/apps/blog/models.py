from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.utils import timezone


User = get_user_model()


class Blog(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="writer"
    )

    title = models.CharField(max_length=60, unique_for_month="pub_date")
    slug = AutoSlugField(populate_from="title", editable=False)
    article = models.TextField()
    share = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    views = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    pub_date = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title

    # def update_views(self, value):
    #     self.views = F("views")
