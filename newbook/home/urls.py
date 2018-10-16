from . import views
from django.urls import path, include

urlpatterns = [

    path('home/', include(views.index), name="index")
]
