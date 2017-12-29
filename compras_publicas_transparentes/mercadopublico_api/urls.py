from django.urls import path

from . import views

app_name = 'mercadopublico_api'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('<str:code>/', views.detail, name='detail'),
    path('list/<int:year>/<int:month>/<int:day>/', views.list, name='list'),
    path('list/', views.list, name='listempty'),
#    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
]
