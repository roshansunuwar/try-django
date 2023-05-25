from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
# def login_view(request):
#     if request.method == "POST":
#         # username = request.POST.get('username')
#         username = request.POST['username']
#         password = request.POST['password']
#         # password = request.POST.get('password')
#         user = authenticate(request, username = username, password = password)
#         if user is None:
#             context = {
#                 'error': "Invalid username or password."
#                 }
#             return render(request, "accounts/login.html", context)
#         login(request, user)
#         # return redirect('/admin') #redirect to the admin page        
#         return redirect('/')    #redirect to the home page
#     return render(request, "accounts/login.html", {})


# AuthenticationForm Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)    
            return redirect('/')    #redirect to the home page
    else:
        form = AuthenticationForm(request)
    context = {
        "form" : form
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')
    return render(request, "accounts/logout.html")

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {
        "form" : form
    }
    return render(request, 'accounts/register.html', context)
