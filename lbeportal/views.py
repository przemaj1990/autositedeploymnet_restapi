from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View

from lbeportal.forms import SiteVendorForm
from lbeportal.models import SiteVendor
from django.views.generic.edit import FormView, FormMixin

from nocportal.forms import CommentForm
from nocportal.models import NocComment

class MainView(View):

    def get(self, request):
        return render(request, 'main.html')


class SiteVendorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'sitevendor_create.html'
    form_class = SiteVendorForm
    queryset = SiteVendor.objects.all()
    success_message = 'Site successfully added!'
    # success_url = reverse_lazy('lbeportal:list')


    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        send_mail('Subject here', 'Here is the message.', 'przemaj1990@gmail.com', ['przemaj1990@gmail.com'], fail_silently=False)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('lbeportal:detail', kwargs={'pk': self.object.pk})



class SiteVendorListView(ListView):
    template_name = 'sitevendor_list.html'
    # queryset = SiteVendor.objects.all().order_by('-pk')
    paginate_by = 20
    ordering = ['-pk']
    model = SiteVendor

    # Def that allow search to work
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = SiteVendor.objects.filter(
                Q(site_code__icontains=query)|
                Q(address__icontains=query)
            ).distinct()
        else:
            object_list = SiteVendor.objects.all()
        return object_list



class SiteVendorDetailView(FormMixin, DetailView):
    template_name = 'sitevendor_detail.html'
    # queryset = SiteVendor.objects.all()
    model = SiteVendor
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('lbeportal:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(SiteVendorDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'site': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(SiteVendorDetailView, self).form_valid(form)



class SiteVendorUpdateView(UpdateView):
    template_name = 'sitevendor_update.html'
    queryset = SiteVendor.objects.all()
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lbeportal:detail', kwargs={'pk': self.object.pk})

    # template_name_suffix = '_update_form'

class SiteVendorDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'sitevendor_delete.html'
    queryset = SiteVendor.objects.all()

#