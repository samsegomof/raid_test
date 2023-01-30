from django.db import models


class FrameworkModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Фреймворк'
        verbose_name_plural = 'Фреймворки'

    def __str__(self):
        return f'{self.name} - {self.language}'
