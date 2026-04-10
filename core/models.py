from django.db import models

# Create your models here.


class Maktab(models.Model):
    raqam = models.PositiveIntegerField()
    manzil = models.CharField(max_length=56)


class Fanlar(models.Model):
    name = models.CharField(max_length=28)


class Xodim(models.Model):
    name = models.CharField(verbose_name='FIO', max_length=56)
    yonalish = models.ForeignKey(Fanlar, on_delete=models.SET_NULL, null=True)
    age = models.PositiveIntegerField(default=20)
    position = models.CharField(max_length=10, choices=[
        ('MMBIDO', 'manaviyat va marifat ishlari boyicha direktor orinbosari'),
        ('teach', 'oqtuvchi'),
        ('Dir', 'direktor'),
    ])


class Sinf(models.Model):
    nomi = models.CharField(max_length=5)
    manzil = models.ForeignKey(Maktab, on_delete=models.SET_NULL, null=True)
    kurator = models.ForeignKey(Xodim, on_delete=models.SET_NULL, null=True, limit_choices_to={'position': 'teach'})


class Student(models.Model):
    ism = models.CharField(max_length=56)
    familiya = models.CharField(max_length=56)
    otasini_ismi = models.CharField(max_length=56, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    sinf = models.ForeignKey(Sinf, on_delete=models.SET_NULL, null=True)
    birth_date = models.DateField()
    last_attend = models.DateTimeField(verbose_name='oxirgi marta darsga kelgan vaqt')
    gender = models.BooleanField(choices=[
        (True, 'Erkak'),
        (True, 'Ayol'),
    ])
    last_updated = models.DateTimeField(auto_now=True)
    joined_date = models.DateTimeField(auto_now_add=True)


