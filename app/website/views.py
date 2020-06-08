from django.shortcuts import render, get_object_or_404
from website.models import *
import logging
logger = logging.getLogger(__name__)


def home(request):

    context = {
        "html": drawSons(None, "")
    }
    return render(request, "html/inicio.html", context)


def pagina(request, pagina_slug):
    pagina = get_object_or_404(Pagina, slug=pagina_slug)
    context = {
        "Pagina": pagina,
        "html": drawSons(None, ""),
        "Theme": "themes/" + str(pagina.design) + ".css",
        "Posts": Post.objects.filter(pagina=pagina),
    }
    return render(request, "html/pagina.html", context)


def drawSons(pai, html):

    paginas = getSons(pai)
    if paginas.exists() == False:
        return html
    html += "<ul>"

    for pagina in paginas:
        html += "<li><a href=/"+str(pagina.slug)+">"
        html += pagina.nome
        html += "</a></li>"
        html = drawSons(pagina, html)
    html += "</ul>"
    return html


def getSons(parent):
    sons = Pagina.objects.filter(pai=parent)
    return sons
