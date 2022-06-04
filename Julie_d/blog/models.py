from django.db import models


class Post(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    date = models.DateField('Дата публикации')
    user = models.ForeignKey('new_user.User', on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField('new_user.User', related_name='liked_posts', blank=True)

    def __str__(self):
        return f'Пост: {self.title}'

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
