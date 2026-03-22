from django.shortcuts import render, redirect, get_object_or_404
from .models import User

# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, "home.html", {'users': users})

def show_create(request):
    return render(request, 'create.html')

def create_user(request):
    if request.method == 'POST':
        data = request.POST

        username = data.get('username')
        email = data.get('email')

        User.objects.create(
            username = username,
            email = email,
        )
        return redirect('/')
    return render(request, "create.html")

def show_update(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'update.html', {'user': user})

def update_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        data = request.POST

        username = data.get('username')
        email = data.get('email')

        user.username = username
        user.email = email
        user.save()
        return redirect('/')
    return render(request, 'update.html', {'user': user})

def delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('/')