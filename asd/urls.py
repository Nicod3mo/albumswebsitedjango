from django.urls import path
from .views import mostrar, agregar, detallar, actualizar, eliminar

urlpatterns = [
    path('', mostrar.as_view(), name="album_Listar"),
    path('agregaralbum/',agregar.as_view(), name="album_Agregar"),
    path('album/<int:pk>', detallar.as_view(), name="album_Detallar"),
    path('album/<int:pk>/actualizar', actualizar.as_view(), name="album_Actualizar"),
    path('album/<int:pk>/eliminar', eliminar.as_view(), name="album_Eliminar"),
]