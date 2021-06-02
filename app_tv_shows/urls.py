from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.main),
    path('shows/new', views.newform),
    path('shows/create', views.create),
    path('shows/<int:show_id>',views.show_info),
    path('<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),
    path('shows/<int:show_id>/destroy', views.delete),
]