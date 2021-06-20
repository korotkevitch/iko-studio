from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from datetime import datetime
from django.views.generic import View
from django.views.generic import ListView
from .models import Funny, FunnyGallery, FunnyMenuFirst, FunnyMenuSecond, FunnyMenuThird, FunnyFeedback, PizzaImages, \
    PizzaMenu, PizzaPopular, PizzaGallery, PizzaMenu12, PizzaPersonal, PizzaFeedback, PizzaInfo, VenueText, VenueImage, \
    VenueMenu, VenueTeam, VenueTestimonial, VenueHit, VenueFeedback, VenueRes, VenueThanks, Header, Feedback, \
    CoffeeFeedback, CoffeeInfo, CoffeeMenu, CoffeePopular, CoffeeMenu9, CoffeeGallery, CoffeeTestimonial, FeedbackBuy, \
    FeedbackAdm, KusinaTop, KusinaAbout, KusinaStatistics, KusinaMenu, KusinaTestimonial, KusinaTeam, KusinaReservation, \
    KusinaNewsletter, KusinaInsta, KusinaDownloadMenu, BeeGallery, ConstructoGallery, TmpGallery, Tmpl, Area, \
    FeedbackIndex, BusHead, BusGallery, TransporterHead
from .forms import FunnyUserForm, PizzaUserForm, VenueUserForm, VenueResUserForm, UserForm, CoffeeUserForm, UserFormBuy, \
    UserFormAdm, KusinaReservationForm, KusinaNewsletterForm, UserFormIndex



def base(request):
    areas = Area.objects.all()

    return render(request, "base.html", {'areas': areas,
                                         })


def index(request):
    areas = Area.objects.all()
    templates = Tmpl.objects.all()
    return render(request, "index.html", {'areas': areas,
                                          'templates': templates,
                                          })


def about(request):
    areas = Area.objects.all()
    return render(request, "about.html", {'areas': areas,
                                          })


def catalog(request):
    areas = Area.objects.all()
    templates = Tmpl.objects.all()

    return render(request, "catalog.html", {'areas': areas,
                                            'templates': templates,

                                          })


def faq(request):
    areas = Area.objects.all()
    return render(request, "faq.html", {'areas': areas,
                                          })


def contact(request):
    areas = Area.objects.all()
    return render(request, "contact.html", {'areas': areas,
                                          })


def area(request, slug):
    areas = Area.objects.all()
    current_area = get_object_or_404(Area, slug=slug)
    area_templates = current_area.tmpl_set.all()
    return render(request, "area.html", {'current_area': current_area,
                                         'area_templates': area_templates,
                                         'areas': areas,

                                            })


def tmpl_details(request, slug, **kwargs):
    areas = Area.objects.all()
    current_tmpl = get_object_or_404(Tmpl, slug=slug)
    current_area = current_tmpl.area
    return render(request, "tmpl_details.html", {'current_tmpl': current_tmpl,
                                                 'current_area': current_area,
                                                 'areas': areas,

                                            })


def pizza_details(request):
    template_1 = get_object_or_404(Tmpl, id=1)
    template_2 = get_object_or_404(Tmpl, id=2)
    return render(request, "pizza_details.html", {'template_1': template_1,
                                                'template_2': template_2,

                                          })


def feedback_index(request):
    if request.method == 'POST':
        form = UserFormIndex(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            f = FeedbackIndex(name=name, email=email, subject=subject, message=message)

            f.save()
        return render(request, 'thanks_main.html')

    else:
        form = UserForm()
    return render(request, 'thanks_main.html', {'form': form})



def feedback(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            template_number = form.cleaned_data['template_number']
            massage = form.cleaned_data['massage']

            f = Feedback(fname = fname, lname = lname, email = email, phone = phone, template_number=template_number, massage = massage)

            f.save()
        return render(request, 'thanks_main.html')

    else:
        form = UserForm()
    return render(request, 'thanks_main.html', {'form': form})


def feedback_buy(request):
    if request.method == 'POST':
        form = UserFormBuy(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            template_number = form.cleaned_data['template_number']
            massage = form.cleaned_data['massage']

            f = FeedbackBuy(fname = fname, lname = lname, email = email, phone = phone, template_number=template_number, massage = massage)

            f.save()
        return render(request, 'thanks_main.html')

    else:
        form = UserFormBuy()
    return render(request, 'thanks_main.html', {'form': form})


def feedback_adm(request):
    if request.method == 'POST':
        form = UserFormAdm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            template_number = form.cleaned_data['template_number']
            massage = form.cleaned_data['massage']

            f = FeedbackAdm(fname = fname, lname = lname, email = email, phone = phone, template_number=template_number, massage = massage)

            f.save()
        return render(request, 'thanks_main.html')

    else:
        form = UserFormAdm()
    return render(request, 'thanks_main.html', {'form': form})


def examples(request):
    return render(request, "examples.html")

def restaurant(request):
    funny = get_object_or_404(Funny)
    first_title = funny.first_title
    first_text = funny.first_text
    second_title = funny.second_title
    second_text = funny.second_text
    download_menu = funny.download_menu
    address = funny.address
    work_time = funny.work_time
    contact_phone = funny.contact_phone
    email = funny.email
    foods = FunnyGallery.objects.all()
    all_plates = FunnyMenuFirst.objects.all()
    menu_name = get_object_or_404(FunnyMenuFirst, id=1)
    all_plates_2 = FunnyMenuSecond.objects.all()
    menu_name_2 = get_object_or_404(FunnyMenuSecond, id=1)
    all_plates_3 = FunnyMenuThird.objects.all()
    menu_name_3 = get_object_or_404(FunnyMenuThird, id=1)

    return render(request, "restaurant.html", {'funny': funny,
                                               'first_title': first_title,
                                               'first_text': first_text,
                                               'second_title': second_title,
                                               'second_text': second_text,
                                               'download_menu': download_menu,
                                               'address': address,
                                               'work_time':work_time,
                                               'foods': foods,
                                               'all_plates': all_plates,
                                               'menu_name': menu_name,
                                               'all_plates_2': all_plates_2,
                                               'menu_name_2': menu_name_2,
                                               'all_plates_3': all_plates_3,
                                               'menu_name_3': menu_name_3,
                                               'contact_phone': contact_phone,
                                               'email': email,
                                                })


def funny_feedback(request):
    if request.method == 'POST':
        form = FunnyUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            massage = form.cleaned_data['massage']

            f = FunnyFeedback(name = name, email = email, phone = phone, massage = massage)

            f.save()
        return render(request, 'thanks.html')

    else:
        form = FunnyUserForm()
    return render(request, 'thanks.html', {'form': form})


####### Pizza ########

def pizza(request):
    bg_1 = get_object_or_404(PizzaImages, id=2)
    bg_2 = get_object_or_404(PizzaImages, id=3)
    bg_3 = get_object_or_404(PizzaImages, id=4)
    bg_pizza_1 = get_object_or_404(PizzaImages, id=5)
    bg_pizza_2 = get_object_or_404(PizzaImages, id=6)
    interier = get_object_or_404(PizzaImages, id=7)
    interier_2 = get_object_or_404(PizzaImages, id=8)
    popular_pizza_1 = get_object_or_404(PizzaPopular, id=1)
    popular_pizza_2 = get_object_or_404(PizzaPopular, id=2)
    popular_pizza_3 = get_object_or_404(PizzaPopular, id=3)
    popular_pizza_4 = get_object_or_404(PizzaPopular, id=4)
    popular_pizza_5 = get_object_or_404(PizzaPopular, id=5)
    popular_pizza_6 = get_object_or_404(PizzaPopular, id=6)
    popular_pizza_7 = get_object_or_404(PizzaPopular, id=7)
    popular_pizza_8 = get_object_or_404(PizzaPopular, id=8)
    pizza = get_object_or_404(PizzaInfo)
    menu_pizza_1 = get_object_or_404(PizzaMenu, id=1)
    menu_pizza_2 = get_object_or_404(PizzaMenu, id=2)
    menu_pizza_3 = get_object_or_404(PizzaMenu, id=3)
    menu_pizza_4 = get_object_or_404(PizzaMenu, id=4)
    menu_pizza_5 = get_object_or_404(PizzaMenu, id=5)
    menu_pizza_6 = get_object_or_404(PizzaMenu, id=6)
    menu_pizza_7 = get_object_or_404(PizzaMenu, id=7)
    menu_pizza_8 = get_object_or_404(PizzaMenu, id=8)
    menu_pizza_9 = get_object_or_404(PizzaMenu, id=9)
    menu_pizza_10 = get_object_or_404(PizzaMenu, id=10)
    menu_pizza_11 = get_object_or_404(PizzaMenu, id=11)
    menu_pizza_12 = get_object_or_404(PizzaMenu, id=12)
    gallery_1 = get_object_or_404(PizzaGallery, id=1)
    gallery_2 = get_object_or_404(PizzaGallery, id=2)
    gallery_3 = get_object_or_404(PizzaGallery, id=3)
    gallery_4 = get_object_or_404(PizzaGallery, id=4)
    menu12_1 = get_object_or_404(PizzaMenu12, id=1)
    menu12_2 = get_object_or_404(PizzaMenu12, id=2)
    menu12_3 = get_object_or_404(PizzaMenu12, id=3)
    menu12_4 = get_object_or_404(PizzaMenu12, id=4)
    menu12_5 = get_object_or_404(PizzaMenu12, id=5)
    menu12_6 = get_object_or_404(PizzaMenu12, id=6)
    menu12_7 = get_object_or_404(PizzaMenu12, id=7)
    menu12_8 = get_object_or_404(PizzaMenu12, id=8)
    menu12_9 = get_object_or_404(PizzaMenu12, id=9)
    menu12_10 = get_object_or_404(PizzaMenu12, id=10)
    menu12_11 = get_object_or_404(PizzaMenu12, id=11)
    menu12_12 = get_object_or_404(PizzaMenu12, id=12)
    personal_1 = get_object_or_404(PizzaPersonal, id=1)
    personal_2 = get_object_or_404(PizzaPersonal, id=2)
    personal_3 = get_object_or_404(PizzaPersonal, id=3)
    personal_4 = get_object_or_404(PizzaPersonal, id=4)
    return render(request, 'pizza.html', {'bg_1': bg_1,
                                          'bg_2': bg_2,
                                          'bg_3': bg_3,
                                          'bg_pizza_1': bg_pizza_1,
                                          'bg_pizza_2': bg_pizza_2,
                                          'interier': interier,
                                          'interier_2': interier_2,
                                          'popular_pizza_1': popular_pizza_1,
                                          'popular_pizza_2': popular_pizza_2,
                                          'popular_pizza_3': popular_pizza_3,
                                          'popular_pizza_4': popular_pizza_4,
                                          'popular_pizza_5': popular_pizza_5,
                                          'popular_pizza_6': popular_pizza_6,
                                          'popular_pizza_7': popular_pizza_7,
                                          'popular_pizza_8': popular_pizza_8,
                                          'menu_pizza_1': menu_pizza_1,
                                          'menu_pizza_2': menu_pizza_2,
                                          'menu_pizza_3': menu_pizza_3,
                                          'menu_pizza_4': menu_pizza_4,
                                          'menu_pizza_5': menu_pizza_5,
                                          'menu_pizza_6': menu_pizza_6,
                                          'menu_pizza_7': menu_pizza_7,
                                          'menu_pizza_8': menu_pizza_8,
                                          'menu_pizza_9': menu_pizza_9,
                                          'menu_pizza_10': menu_pizza_10,
                                          'menu_pizza_11': menu_pizza_11,
                                          'menu_pizza_12': menu_pizza_12,
                                          'gallery_1': gallery_1,
                                          'gallery_2': gallery_2,
                                          'gallery_3': gallery_3,
                                          'gallery_4': gallery_4,
                                          'pizza': pizza,
                                          'menu12_1': menu12_1,
                                          'menu12_2': menu12_2,
                                          'menu12_3': menu12_3,
                                          'menu12_4': menu12_4,
                                          'menu12_5': menu12_5,
                                          'menu12_6': menu12_6,
                                          'menu12_7': menu12_7,
                                          'menu12_8': menu12_8,
                                          'menu12_9': menu12_9,
                                          'menu12_10': menu12_10,
                                          'menu12_11': menu12_11,
                                          'menu12_12': menu12_12,
                                          'personal_1': personal_1,
                                          'personal_2': personal_2,
                                          'personal_3': personal_3,
                                          'personal_4': personal_4,
                                          })


def pizza_feedback(request):
    if request.method == 'POST':
        form = PizzaUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            massage = form.cleaned_data['massage']

            f = PizzaFeedback(name = name, email = email, phone = phone, massage = massage)

            f.save()
        return render(request, 'thanks_pizza.html')

    else:
        form = PizzaUserForm()
    return render(request, 'thanks_pizza.html', {'form': form})

######## venue #########

def venue(request):
    text = get_object_or_404(VenueText)
    image = get_object_or_404(VenueImage)
    dish_1 = get_object_or_404(VenueMenu, id=1)
    dish_2 = get_object_or_404(VenueMenu, id=2)
    dish_3 = get_object_or_404(VenueMenu, id=3)
    dish_4 = get_object_or_404(VenueMenu, id=4)
    dish_5 = get_object_or_404(VenueMenu, id=5)
    dish_6 = get_object_or_404(VenueMenu, id=6)
    dish_7 = get_object_or_404(VenueMenu, id=7)
    dish_8 = get_object_or_404(VenueMenu, id=8)
    dish_9 = get_object_or_404(VenueMenu, id=9)
    dish_10 = get_object_or_404(VenueMenu, id=10)
    dish_11 = get_object_or_404(VenueMenu, id=11)
    dish_12 = get_object_or_404(VenueMenu, id=12)
    dish_13 = get_object_or_404(VenueMenu, id=13)
    dish_14 = get_object_or_404(VenueMenu, id=14)
    dish_15 = get_object_or_404(VenueMenu, id=15)
    sign_dish_1 = get_object_or_404(VenueMenu, id=16)
    sign_dish_2 = get_object_or_404(VenueMenu, id=17)
    sign_dish_3 = get_object_or_404(VenueMenu, id=18)
    sign_dish_4 = get_object_or_404(VenueMenu, id=19)
    team = get_object_or_404(VenueTeam)
    testimonials = VenueTestimonial.objects.all()
    testi = get_object_or_404(VenueTestimonial, id=1)
    hit = get_object_or_404(VenueHit)
    return render(request, "venue.html", {'text': text,
                                          'image': image,
                                          'dish_1': dish_1,
                                          'dish_2': dish_2,
                                          'dish_3': dish_3,
                                          'dish_4': dish_4,
                                          'dish_5': dish_5,
                                          'dish_6': dish_6,
                                          'dish_7': dish_7,
                                          'dish_8': dish_8,
                                          'dish_9': dish_9,
                                          'dish_10': dish_10,
                                          'dish_11': dish_11,
                                          'dish_12': dish_12,
                                          'dish_13': dish_13,
                                          'dish_14': dish_14,
                                          'dish_15': dish_15,
                                          'sign_dish_1': sign_dish_1,
                                          'sign_dish_2': sign_dish_2,
                                          'sign_dish_3': sign_dish_3,
                                          'sign_dish_4': sign_dish_4,
                                          'team': team,
                                          'testimonials': testimonials,
                                          'testi': testi,
                                          'hit': hit,
                                        })


def venue_feedback(request):
    if request.method == 'POST':
        thanks = get_object_or_404(VenueThanks)
        form = VenueUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            massage = form.cleaned_data['massage']

            f = VenueFeedback(name = name, email = email, phone = phone, massage = massage)

            f.save()
        return render(request, 'thanks_venue.html', {'thanks': thanks,})

    else:
        form = VenueUserForm()
    return render(request, 'thanks_venue.html', {'form': form,})


def venue_res(request):
    if request.method == 'POST':
        thanks = get_object_or_404(VenueThanks)
        form = VenueResUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            number = form.cleaned_data['number']

            f = VenueRes(name=name, phone=phone, date=date, number=number)

            f.save()
        return render(request, 'thanks_venue.html', {'thanks': thanks})

    else:
        form = VenueResUserForm()
    return render(request, 'thanks_venue.html', {'form': form})



def coffee(request):
    info = get_object_or_404(CoffeeInfo)
    gallery = CoffeeGallery.objects.all()
    menu_1 = get_object_or_404(CoffeeMenu, id=1)
    menu_2 = get_object_or_404(CoffeeMenu, id=2)
    menu_3 = get_object_or_404(CoffeeMenu, id=3)
    menu_4 = get_object_or_404(CoffeeMenu, id=4)
    menu_5 = get_object_or_404(CoffeeMenu, id=5)
    menu_6 = get_object_or_404(CoffeeMenu, id=6)
    menu_7 = get_object_or_404(CoffeeMenu, id=7)
    menu_8 = get_object_or_404(CoffeeMenu, id=8)
    menu_9 = get_object_or_404(CoffeeMenu, id=9)
    menu_10 = get_object_or_404(CoffeeMenu, id=10)
    menu_11 = get_object_or_404(CoffeeMenu, id=11)
    menu_12 = get_object_or_404(CoffeeMenu, id=12)
    menu_13 = get_object_or_404(CoffeeMenu, id=13)
    menu_14 = get_object_or_404(CoffeeMenu, id=14)
    menu_15 = get_object_or_404(CoffeeMenu, id=15)
    menu_16 = get_object_or_404(CoffeeMenu, id=16)
    popular_1 = get_object_or_404(CoffeePopular, id=1)
    popular_2 = get_object_or_404(CoffeePopular, id=2)
    popular_3 = get_object_or_404(CoffeePopular, id=3)
    popular_4 = get_object_or_404(CoffeePopular, id=4)
    menu9_1 = get_object_or_404(CoffeeMenu9, id=1)
    menu9_2 = get_object_or_404(CoffeeMenu9, id=2)
    menu9_3 = get_object_or_404(CoffeeMenu9, id=3)
    menu9_4 = get_object_or_404(CoffeeMenu9, id=4)
    menu9_5 = get_object_or_404(CoffeeMenu9, id=5)
    menu9_6 = get_object_or_404(CoffeeMenu9, id=6)
    menu9_7 = get_object_or_404(CoffeeMenu9, id=7)
    menu9_8 = get_object_or_404(CoffeeMenu9, id=8)
    menu9_9 = get_object_or_404(CoffeeMenu9, id=9)
    testimonial_1 = get_object_or_404(CoffeeTestimonial, id=1)
    testimonial_2 = get_object_or_404(CoffeeTestimonial, id=2)
    testimonial_3 = get_object_or_404(CoffeeTestimonial, id=3)
    testimonial_4 = get_object_or_404(CoffeeTestimonial, id=4)
    testimonial_5 = get_object_or_404(CoffeeTestimonial, id=5)
    return render(request, 'coffee.html', {"info": info,
                                           'gallery': gallery,
                                           'menu_1': menu_1,
                                           'menu_2': menu_2,
                                           'menu_3': menu_3,
                                           'menu_4': menu_4,
                                           'menu_5': menu_5,
                                           'menu_6': menu_6,
                                           'menu_7': menu_7,
                                           'menu_8': menu_8,
                                           'menu_9': menu_9,
                                           'menu_10': menu_10,
                                           'menu_11': menu_11,
                                           'menu_12': menu_12,
                                           'menu_13': menu_13,
                                           'menu_14': menu_14,
                                           'menu_15': menu_15,
                                           'menu_16': menu_16,
                                           'popular_1': popular_1,
                                           'popular_2': popular_2,
                                           'popular_3': popular_3,
                                           'popular_4': popular_4,
                                           'menu9_1': menu9_1,
                                           'menu9_2': menu9_2,
                                           'menu9_3': menu9_3,
                                           'menu9_4': menu9_4,
                                           'menu9_5': menu9_5,
                                           'menu9_6': menu9_6,
                                           'menu9_7': menu9_7,
                                           'menu9_8': menu9_8,
                                           'menu9_9': menu9_9,
                                           'testimonial_1': testimonial_1,
                                           'testimonial_2': testimonial_2,
                                           'testimonial_3': testimonial_3,
                                           'testimonial_4': testimonial_4,
                                           'testimonial_5': testimonial_5,
                                           })


def coffee_feedback(request):
    if request.method == 'POST':
        form = CoffeeUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            phone = form.cleaned_data['phone']
            massage = form.cleaned_data['massage']

            f = CoffeeFeedback(first_name=first_name, second_name=second_name, date=date, time=time, phone=phone, massage=massage)

            f.save()
        return render(request, 'thanks_coffee.html')

    else:
        form = CoffeeUserForm()
    return render(request, 'thanks_coffee.html', {'form': form,})


def kusina(request):
    slide_1 = get_object_or_404(KusinaTop, id=1)
    slide_2 = get_object_or_404(KusinaTop, id=2)
    about = get_object_or_404(KusinaAbout, id=1)
    statistics = get_object_or_404(KusinaStatistics, id=1)
    dish_1 = get_object_or_404(KusinaMenu, id=1)
    dish_2 = get_object_or_404(KusinaMenu, id=2)
    dish_3 = get_object_or_404(KusinaMenu, id=3)
    dish_4 = get_object_or_404(KusinaMenu, id=4)
    dish_5 = get_object_or_404(KusinaMenu, id=5)
    dish_6 = get_object_or_404(KusinaMenu, id=6)
    dish_7 = get_object_or_404(KusinaMenu, id=7)
    dish_8 = get_object_or_404(KusinaMenu, id=8)
    dish_9 = get_object_or_404(KusinaMenu, id=9)
    dish_10 = get_object_or_404(KusinaMenu, id=10)
    dish_11 = get_object_or_404(KusinaMenu, id=11)
    dish_12 = get_object_or_404(KusinaMenu, id=12)
    dish_13 = get_object_or_404(KusinaMenu, id=13)
    dish_14 = get_object_or_404(KusinaMenu, id=14)
    dish_15 = get_object_or_404(KusinaMenu, id=15)
    dish_16 = get_object_or_404(KusinaMenu, id=16)
    dish_17 = get_object_or_404(KusinaMenu, id=17)
    dish_18 = get_object_or_404(KusinaMenu, id=18)
    testimonials = KusinaTestimonial.objects.all()
    team = KusinaTeam.objects.all()
    insta_1 = get_object_or_404(KusinaInsta, id=1)
    insta_2 = get_object_or_404(KusinaInsta, id=2)
    insta_3 = get_object_or_404(KusinaInsta, id=3)
    insta_4 = get_object_or_404(KusinaInsta, id=4)
    insta_5 = get_object_or_404(KusinaInsta, id=5)
    insta_6 = get_object_or_404(KusinaInsta, id=6)
    download_menu = get_object_or_404(KusinaDownloadMenu, id=1)

    return render(request, 'kusina.html', {'slide_1': slide_1,
                                          'slide_2': slide_2,
                                          'about': about,
                                          'statistics': statistics,
                                          'dish_1': dish_1,
                                          'dish_2': dish_2,
                                          'dish_3': dish_3,
                                          'dish_4': dish_4,
                                          'dish_5': dish_5,
                                          'dish_6': dish_6,
                                          'dish_7': dish_7,
                                          'dish_8': dish_8,
                                          'dish_9': dish_9,
                                          'dish_10': dish_10,
                                          'dish_11': dish_11,
                                          'dish_12': dish_12,
                                          'dish_13': dish_13,
                                          'dish_14': dish_14,
                                          'dish_15': dish_15,
                                          'dish_16': dish_16,
                                          'dish_17': dish_17,
                                          'dish_18': dish_18,
                                          'testimonials': testimonials,
                                          'team': team,
                                          'insta_1': insta_1,
                                          'insta_2': insta_2,
                                          'insta_3': insta_3,
                                          'insta_4': insta_4,
                                          'insta_5': insta_5,
                                          'insta_6': insta_6,
                                          'download_menu': download_menu,

    })


def kusina_reservation(request):
    if request.method == 'POST':
        form = KusinaReservationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            phone = form.cleaned_data['phone']
            person = form.cleaned_data['person']

            f = KusinaReservation(first_name=first_name, second_name=second_name, date=date, time=time, phone=phone, person=person)

            f.save()
        return render(request, 'thanks_kusina.html')

    else:
        form = KusinaReservationForm()
    return render(request, 'thanks_kusina.html', {'form': form,})


def kusina_newsletters(request):
    if request.method == 'POST':
        form = KusinaNewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            f = KusinaNewsletter(email=email)

            f.save()
        return render(request, 'thanks_kusina_email.html')

    else:
        form = KusinaNewsletterForm()
    return render(request, 'thanks_kusina_email.html', {'form': form,})


def resta(request):
    return render(request, "resta.html")


def buri(request):
    return render(request, "buri.html")


def foodfun(request):
    return render(request, "foodfun.html")


def bee(request):
    gallery = BeeGallery.objects.all()
    return render(request, "bee.html", {'gallery': gallery,
                                        })


def constructo(request):
    gallery_1 = get_object_or_404(ConstructoGallery, id=1)
    gallery_2 = get_object_or_404(ConstructoGallery, id=2)
    gallery_3 = get_object_or_404(ConstructoGallery, id=3)
    gallery_4 = get_object_or_404(ConstructoGallery, id=4)
    gallery_5 = get_object_or_404(ConstructoGallery, id=5)
    gallery_6 = get_object_or_404(ConstructoGallery, id=6)
    gallery_7 = get_object_or_404(ConstructoGallery, id=7)
    gallery_8 = get_object_or_404(ConstructoGallery, id=8)
    return render(request, "constructo.html", {'gallery_1': gallery_1,
                                               'gallery_2': gallery_2,
                                               'gallery_3': gallery_3,
                                               'gallery_4': gallery_4,
                                               'gallery_5': gallery_5,
                                               'gallery_6': gallery_6,
                                               'gallery_7': gallery_7,
                                               'gallery_8': gallery_8,

                                               })


def webuilder(request):
    return render(request, "webuilder.html")


class BusView(ListView):
    context_object_name = 'bus'
    template_name = 'bus.html'
    queryset = BusHead.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bus_gallery_list'] = BusGallery.objects.all()
        return context


class TransportersView(ListView):
    context_object_name = 'transporters'
    template_name = 'transporters.html'
    queryset = TransporterHead.objects.all()





