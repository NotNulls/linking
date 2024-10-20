from django.shortcuts import render, redirect
from .forms import CategoryForm, LinkForm
from .models import Category, Link
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            # it will create an object but it would not store into the database
            link = form.save(commit=False)
            link.created_by = request.user
            link.save()

            return redirect('/')

    else:
        form = CategoryForm()
    return render(request, 'link/create_category.html', {'form': form})


@login_required
def create_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            # it will create an object, so it would not store into the database
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()

            return redirect('/')

    else:
        form = LinkForm()
        # overriding form from user request access
        form.fields['category'].queryset = Category.objects.filter(created_by=request.user)

    return render(request, 'link/create_link.html', {'form': form, 'title': 'Create link'})


def links(request):
    links = Link.objects.filter(created_by=request.user)

    return render(request, 'link/links.html', {'links': links, 'category': category})
