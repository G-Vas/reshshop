from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Seed, Category, SubCategory


class ProdListMixin:
    def get_prod_list(self):
        return Seed.objects.all()

    def get_subcategory(self):
        return SubCategory.objects.all()

    def get_category_list(self):
        return Category.objects.all()

    def get_seed_list(self):
        return Seed.objects.all()


class About(ProdListMixin, View):
    def get(self, request):
        return render(request, 'CatalogApp/about.html')


class Checkout(ProdListMixin, View):
    def get(self, request):
        return render(request, 'CatalogApp/checkout.html')


class Contact(ProdListMixin, View):
    def get(self, request):
        return render(request, 'CatalogApp/contact.html')


class Faqs(ProdListMixin, View):
    def get(self, request):
        return render(request, 'CatalogApp/faqs.html')


class Index(ProdListMixin, ListView):
    paginate_by = 8
    ordering = ['-id']
    model = Seed
    queryset = Seed.objects.filter(draft=False)
    template_name = "CatalogApp/index.html"


class SeedDetail(ProdListMixin, DetailView):
    model = Seed
    slug_field = "url"
    template_name = 'CatalogApp/productdetail.html'


class FilterSeedView(ProdListMixin, ListView):
    template_name = "CatalogApp/index.html"
    paginate_by = 8
    ordering = ['-id']

    def get_queryset(self):
        queryset = Seed.objects.filter(
            Q(sub_category__in=self.request.GET.getlist("sub_category")) |
            Q(category__in=self.request.GET.getlist("category"))
        ).order_by("-id")
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["sub_category"] = ''.join([f"sub_category={x}&" for x in self.request.GET.getlist("sub_category")])
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        return context
