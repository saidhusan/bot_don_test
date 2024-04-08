from django.urls import path
from . import views

urlpatterns = [
  path('getpost/', views.telegram_bot, name='telegram_bot'),
  path('setwebhook/', views.webhook, name='web_hook'),
  path('startbot/', views.StartBot, name='start_bot'),

]