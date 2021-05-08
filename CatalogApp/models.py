from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    """Подкатегории"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Manufacturer(models.Model):
    name = models.CharField("Название", max_length=100)
    country = models.CharField("Страна", max_length=100)
    description = models.TextField("Описание", max_length=400, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Seed(models.Model):
    """Семена"""
    title = models.CharField("Название", max_length=100)
    tagline = models.TextField("Краткое описсание", max_length=400, default='')
    description = models.TextField("Описание")
    price = models.FloatField("Цена", default=10.50)
    number_of_seeds = models.IntegerField("количество семян", default=1000)
    poster = models.ImageField("Постер", upload_to="seed_posters/")
    country = models.CharField("Страна", max_length=30)
    sub_category = models.ManyToManyField(SubCategory, verbose_name="Подкатегории")
    purpose = models.CharField("Предназначение", max_length=100, default='Корм')
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("seed_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Семена"
        verbose_name_plural = "Семена"


class SeedPhotos(models.Model):
    """Изображеия"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="seed_photos/")
    movie = models.ForeignKey(Seed, verbose_name="Продукт", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображеия"
