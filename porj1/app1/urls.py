from django.urls import path
from .import views


urlpatterns = [
    path('add/',views.addview),
    path('show/',views.showview),
    path('update/<i>',views.updateview),
    path('delete/<i>',views.deleteview),
]