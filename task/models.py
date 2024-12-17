from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(blank=False, null=False, verbose_name='Описание')
    is_complited = models.BooleanField(default=False, blank=True, verbose_name='Выполнено')
    is_created = models.DateTimeField(auto_now_add=True, blank = True, verbose_name='Создано')
    class Meta:
        db_table = 'Task'
        
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    def __str__(self):
        return f"{self.title} {self.description}"
