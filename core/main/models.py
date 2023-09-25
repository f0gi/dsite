from django.db import models


class Forms(models.Model):
    title = models.CharField('Название анкеты', max_length=50, default='Анкета')
    name = models.CharField('Имя', max_length=50)
    age = models.IntegerField('Возраст')
    comment = models.TextField('Комментарий', max_length=200)
    date = models.DateTimeField('Время', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Form'