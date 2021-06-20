"""ikostudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from studio import views
from django.conf.urls.static import static
from django.conf import settings
from django.db import models
from studio.views import BusView, TransportersView
from django.contrib.sitemaps.views import sitemap

admin.site.site_header = 'iko-studio.com'  # Вместо "Администрирование Django" в админке

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('base', views.base, name="base"),
    path('feedback', views.feedback, name="feedback"),
    path('feedback_index', views.feedback_index, name="feedback_index"),
    path('feedback_buy', views.feedback_buy, name="feedback_buy"),
    path('feedback_adm', views.feedback_adm, name="feedback_adm"),
    path('examples', views.examples, name="examples"),
    path('demo/restaurant', views.restaurant, name="restaurant"),
    path('demo/funny_feedback', views.funny_feedback, name="funny_feedback"),
    path('demo/pizza', views.pizza, name="pizza"),
    path('demo/pizza_feedback', views.pizza_feedback, name="pizza_feedback"),
    path('demo/venue', views.venue, name="venue"),
    path('demo/venue_feedback', views.venue_feedback, name="venue_feedback"),
    path('demo/venue_res', views.venue_res, name="venue_res"),
    path('demo/coffee', views.coffee, name="coffee"),
    path('demo/coffee_feedback', views.coffee_feedback, name="coffee_feedback"),
    path('demo/kusina', views.kusina, name="kusina"),
    path('demo/kusina_reservation', views.kusina_reservation, name="kusina_reservation"),
    path('demo/kusina_newsletters', views.kusina_newsletters, name="kusina_newsletters"),
    path('demo/resta', views.resta, name="resta"),
    path('demo/buri', views.buri, name="buri"),
    path('demo/foodfun', views.foodfun, name="foodfun"),
    path('demo/bee', views.bee, name="bee"),
    path('demo/constructo', views.constructo, name="constructo"),
    path('demo/webuilder', views.webuilder, name="webuilder"),
    path('demo/bus', BusView.as_view(), name="bus"),
    path('demo/transporters', TransportersView.as_view(), name="transporters"),
    path('pizza_details', views.pizza_details, name="pizza_details"),

    path('about', views.about, name="about"),
    path('catalog', views.catalog, name="catalog"),
    path('faq', views.faq, name="faq"),
    path('contact', views.contact, name="contact"),
    re_path(r'^catalog/(?P<slug>[-\w]+)/$', views.area, name="area"),  # шаблоны сферы деятельности
    re_path(r'^catalog/(?P<tmpl_slug>[-\w]+)/(?P<slug>[-\w]+)/$', views.tmpl_details, name="tmpl_details"),  # шаблон


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
