from .models import ExampleDetail, Price


# def example(request):
#     return {'all_examples': ExampleDetail.objects.all().filter(is_activated=True)}


def price(request):
    return {'all_prices': Price.objects.all()}
