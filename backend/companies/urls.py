from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, CurrencyViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'currencies', CurrencyViewSet)

urlpatterns = router.urls
