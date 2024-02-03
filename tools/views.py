from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def base(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'tools/base.html', {'posts': posts})