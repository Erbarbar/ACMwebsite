from django.db import models

THEMES = [
    ("red", "red"),
    ("blue", "blue"),
]


class Pagina(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    pai = models.ForeignKey(
        'Pagina',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="filhos",
        related_query_name="filho",
    )
    design = models.CharField(max_length=100, choices=THEMES, default="blue")

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=500)
    texto = models.TextField()
    pagina = models.ForeignKey(
        'Pagina',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="posts",
        related_query_name="post"
    )
