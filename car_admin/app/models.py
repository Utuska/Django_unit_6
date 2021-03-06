from django.db import models


class Car(models.Model):
    brand = models.CharField("бренд", max_length=50)
    model = models.CharField("модель", max_length=50)

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()



    class Meta:
        verbose_name = "машина"
        verbose_name_plural = "машины"
        ordering = ["id"]


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField("описание", max_length=100)
    text = models.TextField("текст")

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name = "обзор"
        verbose_name_plural = "обзоры"
        ordering = ["id"]