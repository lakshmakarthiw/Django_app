from django.conf.urls import url
from service_app import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
]