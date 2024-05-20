from django.shortcuts import render
from .models import Facility
# import products
from .forms import LoginUserForm, RefisterUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def services(request):
    facility = Facility.objects.all()
    data = {
        'title': 'Наши услуги',
        'facility': facility
    }
    return render(request, "main/services.html", data)


def contacts(request):
    return render(request, "main/contacts.html", {'title': 'Контакты'})


def about(request):
    return render(request, "main/about.html", {'title': 'О нас'})


def register(request):
    if request.method == "POST":
        form = RefisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, "main/register_done.html", {'title': 'Регистрация sucsses'})
    else:
        form = RefisterUserForm()
    return render(request, "main/register.html", {'title': 'Регистрация', 'form': form})


# def login(request):
#     form = AuthenticationForm
#     return render(request, "main/login.html", {'title':'Вход'})

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('services')



