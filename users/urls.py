from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registro/', views.registro, name='registro'),
    path('turnos/', views.turnos, name='turnos'),
    path('inventario/', views.inventario, name='inventario'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('registrar-uso-producto/', views.registrar_uso_producto, name='registrar_uso_producto'),
    path('historial-uso', views.historial_uso, name='historial_uso'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)