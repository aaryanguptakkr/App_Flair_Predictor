from django.contrib import admin
from app.views import *
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('', uploadView, name='index'),
    path('automated_testing/', FileUploadView.as_view(), name='test'),
    # url(r'^api/', views.ContactList.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
