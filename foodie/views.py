from django.shortcuts import render
from foodie.models import items
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from PIL import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required()
def gpage(request):
    context = {
        'items': items.objects.all()
    }
    return render(request, 'foodie/dashboard.html', context)


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = items
    fields = ['title', 'img', 'desc', 'price']
    success_url = '/'

    def form_valid(self, form):
        form.instance.chef = self.request.user
        return super().form_valid(form)



def login(request):
    return render(request, 'foodie/login.html')