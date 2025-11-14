# Em latinder_proj/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView # Importe isto

urlpatterns = [
    path('admin/', admin.site.urls),

    # PASSO 1: A nova landing page pública dela na raiz do site
    path('', TemplateView.as_view(template_name='registration/index.html'), name='landing_page'),

    # PASSO 2: Mover todo o nosso app funcional para dentro de /app/
    path('app/', include('accounts.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)