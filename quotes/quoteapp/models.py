from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    fullname = models.CharField(max_length=25, null=False)
    born_date = models.DateField(null=True)
    born_location = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    # quote = models.CharField(max_length=300, null=False)
    quote = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    # created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.quote}"
