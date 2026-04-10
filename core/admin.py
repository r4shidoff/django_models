from django.contrib import admin
from .models import Sinf, Student, Xodim, Maktab, Fanlar

# Register your models here.

admin.site.register(Maktab)
admin.site.register(Student)
admin.site.register(Sinf)
admin.site.register(Fanlar)
admin.site.register(Xodim)

