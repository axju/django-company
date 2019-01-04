from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, FormView
from django.views import View

from company.models import Feature, Headline, Product
from company.forms import RequestForm


class IndexView(View):
    def get(self, request):
        content = {
            'headlines': Headline.objects.all(),
            'features': Feature.objects.all(),
        }
        return render(request, 'company/index.html', content)


class FeatureDetailView(DetailView):
    model = Feature

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jumbotronimages'] = self.object.images.filter(jumbotron=True)
        return context

class FeatureListView(ListView):
    model = Feature
    paginate_by = 100


class ProductDetailView(FormView):
    success_url = '/'

    template_name = 'company/product_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = get_object_or_404(Product, pk=kwargs.get('pk', -1))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        context['jumbotronimages'] = self.object.images.filter(jumbotron=True)
        return context

    def get_form(self, form_class=None):
        form = RequestForm(self.request.POST or None, product=self.object)
        return form

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
