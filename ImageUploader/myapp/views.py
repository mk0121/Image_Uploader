from django.shortcuts import render
from .forms import ImageForm
from .models import Image


# Create your views here.

def home(r):
    if r.method == 'POST':
        form = ImageForm(r.POST, r.FILES)
        if form.is_valid():
            form.save()
    img = Image.objects.all()
    form = ImageForm()
    return render(r, 'myapp/home.html', {'form': form, 'img': img})
