from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('medecins/', include('medecins.urls', namespace="medecin")),
    path('services/', include('services.urls', namespace="services")),
    path('clinique/', include("clinique.urls", namespace="clinique")),
    path('patients/', include('patients.urls', namespace="patients")),
    path('consultations/', include('consulations.urls', namespace="consulations")),

]
