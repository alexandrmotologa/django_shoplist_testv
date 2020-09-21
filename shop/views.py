from django.shortcuts import render
from .models import Product
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class ShowMain(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'product'
    ordering = ['-date_add']

    def get_context_data(self, **kwargs):
        now = timezone.now().strftime("%Y-%m-%d %H:%M")
        ctx = super(ShowMain, self).get_context_data(**kwargs)
        ctx['title'] = 'Home Page'
        ctx['time'] = now
        return ctx


class DeleteProductView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author_post:
            return True
        return False


class DetailsShowMain(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        now = timezone.now().strftime("%Y-%m-%d %H:%M")
        ctx = super(DetailsShowMain, self).get_context_data(**kwargs)
        ctx['title'] = Product.objects.filter(pk=self.kwargs['pk']).first()
        ctx['time'] = now
        return ctx


class CreateShowMain(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'author', 'description', 'date_published', 'cover']


    def form_valid(self, form):
        form.instance.author_post = self.request.user
        return super().form_valid(form)


class UpdateShowMain(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'author', 'description', 'date_published', 'cover']


    def form_valid(self, form):
        form.instance.author_post = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author_post:
            return True
        return False

def order(request):
    return render(request, 'shop/order.html')
