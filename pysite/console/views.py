from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserProfileForm
from .weather import fetchWeather
from .music import play, stop
# Create your views here.
@login_required()
def index(request):
    return render(request, 'console/index.html')
@login_required
def weather(request):
    text, temp = fetchWeather("成都")
    tips = "多喝热水"
    return render(request, 'console/weather.html',context={'text':text, 'temperature':temp, "tips":tips})

@login_required()
def music(request):
    return render(request, 'console/music.html')



@login_required
def play_music(request):
    return 

@login_required
def stop_music(request):
    return 


@login_required()
def about(request):
    return render(request, 'console/about.html')
    


def register(request):
    # record the register result
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # set user's form data to database
            user = user_form.save()
            user.set_password(user.password)
            user.save() 
            
            profile = profile_form.save()
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'console/register.html',
                    {'user_form':user_form, 'profile_form':profile_form,'registered':registered} )

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/console/')
            else:
                # return error page
                return HttpResponse("账号密码错误.")
        else:
            # return invalid login
            print("非法的账户：{0},{1}".format(username,password))
            return HttpResponse("非法的登录.")
    else:
        return render(request, 'console/login.html')

@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/console/")

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def clock_in(request):
    return render(request, "console/clock_in.html")

