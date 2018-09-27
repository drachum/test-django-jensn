from rest_framework import routers
from .views import CompanyViewSet

router = routers.SimpleRouter()
router.register(
    r'company', CompanyViewSet, base_name='company'
)

urlpatterns = router.urls
