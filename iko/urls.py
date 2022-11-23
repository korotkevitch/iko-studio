from django.contrib import admin
from django.urls import path, include
from studio import views
from studio.views import IndexView, ContactFormView
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = 'iko-studio.com'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('examples/', include('studio.urls')),
    path('about', TemplateView.as_view(template_name='studio/about.html')),
    path('contact', TemplateView.as_view(template_name='studio/contact.html')),
    path('contact_form', ContactFormView.as_view(), name="contact_form"),
    path('thanks', TemplateView.as_view(template_name='studio/thanks.html')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
