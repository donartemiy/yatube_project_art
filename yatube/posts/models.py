from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Дата')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Текст', help_text='Введите текст поста')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться пост'
    )
    # Поле для картинки (необязательное) 
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )
    comments = models.ForiengKey(
        'Comment', 
        on_delete= models.CASCADE,
        verbose_name='Комментарий'
    )
    # Аргумент upload_to указывает директорию, 
    # в которую будут загружаться пользовательские файлы. 

    class Meta:
        ordering = ['-pub_date']
        default_related_name = 'posts_rname'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:15]

class Comment(models.Model):
    post = models.SlugField(unique=True, verbose_name='Ссылка'),
    author =  models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    ),
    text = models.TextField(verbose_name='Текст', help_text='Введите текст поста'),
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        default_related_name = 'comment_rname'

    def __str__(self):
        return self.text
