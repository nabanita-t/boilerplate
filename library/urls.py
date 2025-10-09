from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library import views as library_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
# router.register(r'books', BookViewSet, basename='book')
router.register(r'table', library_views.TableAPIView, basename='table')
router.register(r'table-reservation', library_views.TableReservationAPIView, basename='table-reservation')

# router.register('profile', BookViewSet, basename='books-CRUD'),

urlpatterns = [
    path('', include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

]
