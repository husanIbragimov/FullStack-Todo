from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Todo(models.Model):
    STATUS = {
        (0, _('New')),
        (1, _('Process')),
        (2, _('Completed')),
        (3, _('Canceled')),
    }

    PRIORITY = {
        (0, _('None')),
        (1, _('Low')),
        (2, _('Medium')),
        (3, _('High')),
    }

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Logo(models.Model):
    image = models.ImageField(upload_to='logo/')
