from django.urls import path
from myevents import views

app_name = 'myevents'

urlpatterns = [
	path('', views.index, name='index'),
	path('table_view/', views.table_view, name='table_view'),
    path('about/', views.about, name='about'),
    path('add_event/', views.add_event, name='add_event'),
    path('subset/', views.SubsetView.as_view(), name='subset'),
    path('event/<int:event_id>/', views.show_event, name='show_event'),
    path('event/<int:event_id>/edit', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete, name='delete'),
]


