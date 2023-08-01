from django.urls import path, include


from .views import *


urlpatterns = [
        
    path('', index, name="Inicio"),

    path('Articulos', articulos, name="Articulos"),

    path('Quienes somos', quienessomos, name="Quienes somos"),

    path('Presupuestos', presupuestos, name="Presupuestos"),

    path('Contacto', contacto, name="Contacto"),

    path('contactoform2', contactoform2, name="contactoform2"),

]