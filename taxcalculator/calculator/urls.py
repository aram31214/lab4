from django.urls import path
from . import views

urlpatterens[

path('',views.index,name='index'),
path('<int:amount>/',views.calculate_tax,name='calculate_tax'),

path('<taxrate>/',views.show,name='show'),

]