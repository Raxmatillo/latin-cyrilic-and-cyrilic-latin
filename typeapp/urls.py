from django.urls import path
from . views import index, tocyrillic, tolatin

urlpatterns = [
	path('', index, name = 'index'),
	path('tocyrillic/', tocyrillic, name = 'tocyrillic'),
	path('tolatin/', tolatin, name = 'tolatin'),
	]