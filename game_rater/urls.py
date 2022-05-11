"""game_rater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from lib2to3.pgen2.token import SLASH
from rest_framework import routers
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from game_rater_api.views.auth import login_user, register_user
from game_rater_api.views.category_views import CategoryView
from game_rater_api.views.game_views import GameView


router = routers.DefaultRouter(trailing_slash = False)

router.register(r'games', GameView, 'games')
router.register(r'categories', CategoryView, "cats")


urlpatterns = [
    # path listens for the first parameter and then invokes the second parameter
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    # if the route is not one of the built in routes above, look to the ones definied outside of the url patterns
    path('', include(router.urls))
]
