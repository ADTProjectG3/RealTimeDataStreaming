from django.contrib import admin
from django.urls import path
from chartjs import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.HomeView.as_view()),
	path('api', views.ChartData.as_view()),
	path('pointdata', views.PointData.as_view()),

]
