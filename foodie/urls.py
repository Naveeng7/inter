from django.urls import path
from foodie import views as f_views
from foodie.views import ItemCreateView, ItemUpdateView, ItemDeleteView, ItemDetailedView


urlpatterns = [
    path('', f_views.gpage, name='greeting'),
    path('item/new/', ItemCreateView.as_view(), name='new'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(template_name='foodie/confirm_delete.html'), name='delete'),
    path('item/<int:pk>/', ItemDetailedView.as_view(), name='detailed')
]