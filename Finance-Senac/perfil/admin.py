from django.contrib import admin

# Register your models here.
from perfil.models import Conta, categoria

admin.site.register(Conta)
admin.site.register(categoria)