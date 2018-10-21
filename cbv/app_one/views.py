from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from app_one import models
from django.urls import reverse_lazy

# Create your views here.

class indexView(TemplateView):
    template_name='index.html'

    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['injectme']='hey deer im being injected!!!'
    #     return context

class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'app_one/school_detail.html'

    context_object_name = 'school_detail'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('app_one:list')