from django.db import models
from ckeditor.fields import RichTextField

class ContactModel(models.Model):
    """Обратная связь"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Присланные вопросы'

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """Модели контактов"""
    icon = models.FileField(upload_to='icons/', blank=True)
    name = RichTextField(blank=True, default='')

    class Meta:
        verbose_name_plural = 'Контактные данные / "Контакты" - текст'



class About(models.Model):
    """Страница о нас"""
    name = models.CharField(max_length=100, blank=True, null=True)
    text = RichTextField()
    mini_text = RichTextField()
    registration = RichTextField(blank=True, default='')

    class Meta:
        verbose_name_plural = '"Обо мне" / Кратко обо мне / регистрация'

    def get_images(self):
        return self.about_images.order_by('id')

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url



class ImageAbout(models.Model):
    """Изображение страницы о нас"""
    image = models.ImageField(upload_to="about/")
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_images")

class Social(models.Model):
    """Соцсети страницы о нас"""
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField(default='')

    class Meta:
        verbose_name_plural = 'Социальные сети'
