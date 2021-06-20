from django import forms
from django.forms import ModelForm
from .models import FunnyFeedback, PizzaFeedback, VenueFeedback, VenueRes, Feedback, CoffeeFeedback, FeedbackBuy, FeedbackAdm, \
    KusinaReservation, KusinaNewsletter, FeedbackIndex


class UserFormIndex(forms.Form):
    name = forms.CharField(label = 'Имя', max_length=50, required=False)
    email = forms.EmailField(label = 'Емейл', max_length=50, required=False)
    subject = forms.CharField(label='Тема', max_length=50, required=False)
    message = forms.CharField(label = 'Сообщение', max_length=500, widget=forms.Textarea, required=False)


class UserForm(forms.Form):
    fname = forms.CharField(label = 'Имя', max_length=50, required=False)
    lname = forms.CharField(label='Фамилия', max_length=50, required=False)
    email = forms.EmailField(label = 'Емейл', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=False)
    template_number = forms.CharField(label='Номер шаблона', max_length=50, required=False)
    massage = forms.CharField(label = 'Сообщение', max_length=500, widget=forms.Textarea, required=False)


class UserFormBuy(forms.Form):
    fname = forms.CharField(label = 'Имя', max_length=50, required=False)
    lname = forms.CharField(label='Фамилия', max_length=50, required=False)
    email = forms.EmailField(label = 'Емейл', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=False)
    template_number = forms.CharField(label='Номер шаблона', max_length=50, required=False)
    massage = forms.CharField(label = 'Сообщение', max_length=500, widget=forms.Textarea, required=False)


class UserFormAdm(forms.Form):
    fname = forms.CharField(label = 'Имя', max_length=50, required=False)
    lname = forms.CharField(label='Фамилия', max_length=50, required=False)
    email = forms.EmailField(label = 'Емейл', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=False)
    template_number = forms.CharField(label='Номер шаблона', max_length=50, required=False)
    massage = forms.CharField(label = 'Сообщение', max_length=500, widget=forms.Textarea, required=False)


class FunnyUserForm(forms.Form):
    name = forms.CharField(label = 'Имя', max_length=50, required=False)
    email = forms.EmailField(label = 'Емейл', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=True)
    massage = forms.CharField(label = 'Сообщение', max_length=500, widget=forms.Textarea, required=False)


class PizzaUserForm(forms.Form):
    name = forms.CharField(label = 'Имя', max_length=50, required=False)
    email = forms.EmailField(label = 'Емейл', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=True)
    massage = forms.CharField(label = 'Сообщение', max_length=500, widget=forms.Textarea, required=False)


class VenueUserForm(forms.Form):
    name = forms.CharField(label = 'Имя', max_length=50, required=False)
    email = forms.EmailField(label = 'Емейл', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=True)
    massage = forms.CharField(label = 'Сообщение', max_length=500, widget=forms.Textarea, required=False)


class VenueResUserForm(forms.Form):
    name = forms.CharField(label = 'ФИО', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=True)
    date = forms.CharField(label='Дата, время', max_length=50, required=True)
    number = forms.CharField(label = 'Сколько персон', max_length=50, required=True)


class CoffeeUserForm(forms.Form):
    first_name = forms.CharField(label = 'Имя', max_length=50, required=False)
    second_name = forms.CharField(label='Фамилия', max_length=50, required=False)
    date = forms.CharField(label='Дата', max_length=50, required=False)
    time = forms.CharField(label='Время', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=False)
    massage = forms.CharField(label = 'Сообщение', max_length=500, widget=forms.Textarea, required=False)


class KusinaReservationForm(forms.Form):
    first_name = forms.CharField(label = 'Имя', max_length=50, required=False)
    second_name = forms.CharField(label='Фамилия', max_length=50, required=False)
    date = forms.CharField(label='Дата', max_length=50, required=False)
    time = forms.CharField(label='Время', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=False)
    person = forms.CharField(label = 'Персон', max_length=500, widget=forms.Textarea, required=False)


class KusinaNewsletterForm(forms.Form):
    email = forms.EmailField(label = 'Емейл', max_length=50, required=True)