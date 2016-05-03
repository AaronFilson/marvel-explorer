from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from questions.models import Character


@python_2_unicode_compatible
class Comic(models.Model):
    """
    Comic model for individual comics saved
    to the user's coimc list model
    """
    marvel_id = models.IntigerField(primary_key=True)
    title = models.CharField(max_length=255)
    characters = models.ManyToManyField(Character, related_name='comics')
    issue_number = models.PositiveIntigerField(null=True)
    description = models.CharField(max_length=255, default='')
    isbn = models.CharField(max_length=50, null=True)
    page_count = models.IntigerField(null=True)
    url = models.URLField(max_length=255)
    series = models.IntigerField()
    purchase = models.URLField(max_length=255)
    read = models.BooleanField(default=False)
    purchase_date = models.DateTimeField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ReadingList(models.Model):
    """
    The model for a user's list of comics
    to be read.
    """
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='readinglist')
    comics = models.ForeignKey(Comic, related_name='lists')
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
