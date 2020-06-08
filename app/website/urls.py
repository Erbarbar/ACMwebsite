from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('<slug:pagina_slug>',
         pagina,
         name="pagina"),

    path('',
         home,
         name="inicio"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
