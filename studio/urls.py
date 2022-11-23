from django.urls import path
from studio import views
from .views import ExampleListView, ExampleDetailsView


urlpatterns = [
    path('', ExampleListView.as_view(), name='examples'),
    path('<slug:example_slug>/', ExampleDetailsView.as_view(), name='example_details'),
]
