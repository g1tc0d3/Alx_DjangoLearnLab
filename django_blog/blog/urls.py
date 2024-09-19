from views import PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter
router.register('login/', 'register/', 'profile/'
    'Post', PostViewSet, basename= 'Post',
    
    )
    
urlpatterns = router.urls 


