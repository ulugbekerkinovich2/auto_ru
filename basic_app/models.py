from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from write_from_excell import my_func


# Create your models here.
class Mark(models.Model):
    mark_name = models.CharField(max_length=500, default=None, unique=True)

    def __str__(self):
        return self.mark_name

    class Meta:
        db_table = 'mark'


class Model1(models.Model):
    model_name = models.CharField(max_length=500, default='none')
    mark_name = models.ForeignKey(Mark, on_delete=models.CASCADE, verbose_name='mark_name')

    def __str__(self):
        return self.mark_name

    class Meta:
        db_table = 'model1'
        # unique_together = ['model_name', 'mark_name']


class Fuel1(models.Model):
    fuel = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.fuel

    class Meta:
        db_table = 'fuel1'


class Upload_File(models.Model):
    file = models.FileField(upload_to='files/')
    write_file_name = models.CharField(max_length=100, default='excell2023')

    def __str__(self):
        return self.file

    class Meta:
        db_table = 'upload_file'
        verbose_name_plural = 'upload_file'


@receiver(post_save, sender=Upload_File)
def post_save_function(sender, **kwargs):
    return my_func()
