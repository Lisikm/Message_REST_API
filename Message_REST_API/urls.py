"""Message_REST_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from message_app.views import MessageView, MessageUpdateView, MessageCreateView, MessageDestroyView, RegistrationView, \
    ObtainTokenView

urlpatterns = [
    path('message_view/<int:pk>/', MessageView.as_view(), name='message-view'),
    path('message_create/', MessageCreateView.as_view(), name='message-create'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message-update'),
    path('message_destroy/<int:pk>/', MessageDestroyView.as_view(), name='message-destroy'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('obtain_token/', ObtainTokenView.as_view(), name='obtain-token'),
]
