from django.urls import path
from .import views
from .views import *

from django.conf.urls.static import static
from django.conf import  settings
app_name = 'firstapp'

urlpatterns =[
	path('',views.home ,name = "home"),
	path('data/',views.data,name='data'),
	path('search/',views.search,name='search'),
	#path('results/',views.results,name='results'),
	path('results',SearchResultsView.as_view(),name='results')
]

urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)