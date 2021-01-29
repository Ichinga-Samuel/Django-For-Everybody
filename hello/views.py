from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm


class TemplateView(generic.ListView):
    template_name = 'hello/main.html'

    def get_queryset(self):
        pass


def test_session(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del (request.session['num_visits'])
    resp = HttpResponse('view count=' + str(num_visits))
    resp.set_cookie('dj4e_cookie', '3f97b78c', max_age=1000)
    return resp


@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
            username=cd['username'],
            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    next = 'dashboard'
    return render(request, 'registration/login.html', {'form': form, 'next': next})
