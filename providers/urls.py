from rest_framework import routers
from .views import ProviderViewSet, ServiceAreaViewSet

router = routers.DefaultRouter()
router.register('providers', ProviderViewSet, 'providers') # url /providers


urlpatterns = router.urls

# DefaultRouter endpoints:

# ACTION    METHOD      URL

# List      GET         api/{url}
# Create    POST        api/{url}
# Retrieve  GET         api/{url}/{id}
# Update    PUT,PATCH   api/{url}/{id}
# Delete    DELETE      api/{url}/{id}