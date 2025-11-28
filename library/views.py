from django.shortcuts import render,redirect, get_object_or_404
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            messages.success(request, f"'{book.title}' eklendi! ✨")
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    return render(request, 'library/book_detail.html', {'book': book})

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.id_valid():
            form.save()
            messages.success(request, f"'{book_detail}' güncellendi ✏️")
            return redirect('home')
    
    else:
        form = BookForm(instance=book)
    return render(request, 'library/edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f"'{title}' silindi  🗑️")
        return redirect('home')
    return render(request, 'library/delete_book_confirm.html', {'book': book})