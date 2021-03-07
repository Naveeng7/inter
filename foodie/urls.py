from django.urls import path
from foodie import views as f_views
from foodie.views import ItemCreateView, ItemUpdateView, ItemDeleteView


urlpatterns = [
    path('', f_views.gpage, name='greeting'),
    path('item/new/', ItemCreateView.as_view(), name='new'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='update'),
    path('item/<int:k>/delete/', ItemDeleteView.as_view(), name='delete')
]