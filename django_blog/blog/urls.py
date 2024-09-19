from views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter
router.register('Post', PostViewSet, basename= 'Post')

urlpatterns = router.urls 


