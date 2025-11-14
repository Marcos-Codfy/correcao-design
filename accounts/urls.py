# latinder_proj/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView # Importe isto

urlpatterns = [
    path('admin/', admin.site.urls),

    # ROTA 1: A nova landing page pública na raiz
    path('', TemplateView.as_view(template_name='registration/index.html'), name='landing_page'),

    # ROTA 2: Todo o nosso app funcional agora vive dentro de /app/
    path('app/', include('accounts.urls')), 
    path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)