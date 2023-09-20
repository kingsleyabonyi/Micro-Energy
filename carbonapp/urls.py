from django.urls import path
from .views import calc_carbon


urlpatterns = [
    path('calc/', calc_carbon, name="carbon" ),
    # path('register/', register, name='register'),
    # path('login/', login, name='login'),
    # path('logout/', logout, name='logout')
]