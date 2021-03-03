from django.shortcuts import render, redirect
from foodie.models import items
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from foodie.forms import UserRegisterFrom
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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

@login_required()
def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'New client account created')
            return redirect('greeting')
    else:
        form = UserRegisterFrom()
    return render(request, 'foodie/register.html', {'form': form})
