from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import Product, Order
from .forms import OrderForm

class HomeView(FormMixin, ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"
    form_class = OrderForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['necklaces'] = Product.objects.filter(category='Necklace')
        context['rings'] = Product.objects.filter(category='Ring')
        context['earrings'] = Product.objects.filter(category='Earring')
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        product_id = self.request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        order = form.save(commit=False)
        order.product = product
        order.save()
        messages.success(self.request, f"Thank you! Your order for {product.name} has been placed.")
        return super().form_valid(form)
