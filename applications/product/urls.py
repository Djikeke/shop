

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    # path('', ListCreateView.as_view()),
    # path('<int:pk>/', DeleteUpdateRetrieveView.as_view()),
    path('', include(router.urls)),

]