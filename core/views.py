from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from library.models import Book
from django.db.models import Q


# Create your views here.
def home(request):
    filter_type = request.GET.get("filter")
    q = request.GET.get("q","").strip()

    books = Book.objects.all()

    if request.user.is_authenticated:
        books = books.filter(user=request.user)
    else:
        books = books.none()

    if filter_type == "favorites":
        books = books.filter(rating=5)

    if q:
        books = books.filter(
            Q(title__icontains=q) | Q(author__icontains=q)
        )
    
    books = books.order_by('-started_on')
    
    return render(request, "core/home.html",
            {"books": books,
             "filter_type":filter_type,
            "q": q,
            }
    )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form' : form})