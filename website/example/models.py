from django.db import models

class Item(models.Model):
    item_id = models.CharField(max_length=100, unique=True)
    item_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.item_id

    class Meta:
        app_label = 'example'
