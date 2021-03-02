from django.urls import path
from foodie import views as f_views
from foodie.views import ItemCreateView
urlpatterns = [
    path('', f_views.gpage, name='greeting'),
    path('item/new/', ItemCreateView.as_view(), name='new')
]