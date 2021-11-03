
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from django.urls.conf import include


urlpatterns = [

    # URLS para el JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]