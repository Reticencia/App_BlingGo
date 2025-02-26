from django.urls import path
from .views import ProductoGeneric,updateLocation#RegisterView
#Estudiar TOKEN
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('productos/', ProductoGeneric.as_view()),
    path('ubicacion/actualizar/', updateLocation.as_view()),
    #Estudiar esto TOoken
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Renovar token
    #path('register/', RegisterView.as_view(), name='register'),
]
