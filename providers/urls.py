from rest_framework import routers
from .views import ProviderViewSet, ServiceAreaViewSet, CheckServiceAreaApiView

class OptionalTrailingSlashRouter(routers.DefaultRouter):

    def __init__(self, *args, **kwargs): 
        super(routers.DefaultRouter, self).__init__(*args, **kwargs) 
        self.trailing_slash = '/?'

router = OptionalTrailingSlashRouter()
router.register('providers', ProviderViewSet, 'providers') # url /providers
router.register('servicearea', ServiceAreaViewSet, 'servicearea') # url /service_area
router.register('check', CheckServiceAreaApiView, 'check') 


urlpatterns = router.urls

# DefaultRouter endpoints:

# ACTION    METHOD      URL

# List      GET         api/{url}
# Create    POST        api/{url}
# Retrieve  GET         api/{url}/{id}
# Update    PUT,PATCH   api/{url}/{id}
# Delete    DELETE      api/{url}/{id}