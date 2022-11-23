from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.views.generic import View, ListView
from .models import ExampleList, ExampleDetail, ContactForm
from .forms import UserForm
from django.core.mail import BadHeaderError
from django.views.generic.edit import FormView
from django.core.mail import send_mail


class IndexView(ListView):
    template_name = 'index.html'
    queryset = ExampleDetail.objects.all().filter(is_activated=True)
    context_object_name = 'all_examples'


class ExampleListView(ListView):
    template_name = 'studio/examples.html'
    queryset = ExampleList.objects.all()
    context_object_name = 'all_texts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_examples'] = ExampleDetail.objects.all().filter(is_activated=True)
        return context


class ExampleDetailsView(ListView):
    template_name = 'studio/example_details.html'
    context_object_name = 'current_example'

    def get_queryset(self):
        return get_object_or_404(ExampleDetail, slug=self.kwargs['example_slug'])


class ContactFormView(FormView):
    model = ContactForm
    form_class = UserForm
    success_url = 'thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)




# class AreaView(ListView):
#     model = Area
#     template_name = 'studio/area.html'
#
#     def get_context_data(self, **kwargs):
#         self.area = get_object_or_404(Area, slug=self.kwargs['area_slug'])
#         context = super().get_context_data(**kwargs)
#         context['current_area'] = get_object_or_404(Area, slug=self.kwargs['area_slug'])
#         context['current_area_templates'] = Tmpl.objects.filter(area=self.area)
#         return context
#
#
# class TmplDetailsView(ListView):
#     template_name = 'studio/tmpl_details.html'
#     context_object_name = 'current_tmpl'
#
#     def get_queryset(self):
#         return get_object_or_404(Tmpl, slug=self.kwargs['template_slug'])
#
#     def get_context_data(self, **kwargs):
#         self.area = get_object_or_404(Area, slug=self.kwargs['area_slug'])
#         context = super().get_context_data(**kwargs)
#         context['current_area'] = get_object_or_404(Area, slug=self.kwargs['area_slug'])
#         return context