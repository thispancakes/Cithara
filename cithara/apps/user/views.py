from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .models import User


# Create your views here.
MODEL = User

class IndexView(generic.ListView):
    model = MODEL
    template_name = "index.html"
    context_object_name = "users"

    # def get_queryset(self):
    #     return User.objects.order_by("id")

class CreateView(generic.CreateView):
    model = MODEL
    template_name = "create.html"
    fields = [f.name for f in MODEL._meta.get_fields()]

class UpdateView(generic.UpdateView):
    model = MODEL
    template_name = "update.html"
    fields = [f.name for f in MODEL._meta.get_fields()]

# def home(request):
#     users = User.objects.all()
#     return render(request, "index.html", {'users': users})

# def show_create(request):
#     return render(request, 'create.html')

# def show_update(request, id):
#     user = get_object_or_404(User, id=id)
#     return render(request, 'update.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        data = request.POST

        username = data.get('username')
        email = data.get('email')

        User.objects.create(
            username = username,
            email = email,
        )
        return redirect('/users/')
    return render(request, "create.html")

def update_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        data = request.POST

        username = data.get('username')
        email = data.get('email')

        user.username = username
        user.email = email
        user.save()
        return redirect('/users/')
    return render(request, 'update.html', {'user': user})

def delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('/users/')