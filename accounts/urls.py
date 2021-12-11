from django.urls import path
from rest_framework.routers import SimpleRouter

from accounts.views import CreateUserView, LoginUserVIew

router = SimpleRouter()
router.register(prefix=r'accounts', viewset=CreateUserView, basename='user')

urlpatterns = [
    path('login/', LoginUserVIew.as_view())
]

urlpatterns += router.urls
