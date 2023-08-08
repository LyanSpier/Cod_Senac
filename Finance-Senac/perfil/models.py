from django.db import models

# Create your models here.
class categoria(models.Model):
    categoria = models.CharField(max_length=50,null=False,blank=False, verbose_name='categoria')
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0, verbose_name='valor do planejamento')
    
    def __str__(self):
        return self.categoria
    
class Conta(models.Model):
    banco_choices = (
        ('NU', "nubank"),
        ('BB', "Banco do Brasil"),
        ('BD', "Bradesco"),
        ('CX', "Caixa"),
    )
    
    tipo_choices = (
        ('pf','Pessoa Física'),
        ('pJ','Pessoa Jurídica')
    )
    
    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choices)
    tipo = models.CharField(max_length=2,choices=tipo_choices)
    valor = models.FloatField(verbose_name='Valor do deposito')
    icone = models.ImageField(upload_to='Icone')
    
    def __str__(self):
        return self.apelido
    