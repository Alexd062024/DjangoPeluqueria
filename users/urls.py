from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registro/', views.registro, name='registro'),
    path('turnos/', views.turnos, name='turnos'),
    path('inventario/', views.inventario, name='inventario'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)