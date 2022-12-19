from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.authorUser.username

    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'

    def update_rating(self):
        post_rat = self.post_set.aggregate(postRating=Sum('rating'))
        p_rate = 0
        p_rate += post_rat.get('postRating')

        comment_rat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        c_rate = 0
        c_rate += comment_rat.get('commentRating')

        self.ratingAuthor = p_rate * 3 + c_rate
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Имя автора')
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    ]
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE, verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    rating = models.SmallIntegerField(default=0, verbose_name='Рейтинг автора')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return '{}...'.format(self.text[0:125])


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.categoryThrough.name

    class Meta:
        verbose_name = 'Категория поста'
        verbose_name_plural = 'Категории постов'


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
