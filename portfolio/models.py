from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="Projects")
    link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    createDate = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    modifyDate = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-createDate"]

    def __str__(self):
        return self.title
