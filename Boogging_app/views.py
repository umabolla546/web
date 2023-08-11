from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache import cache





def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()
    return render(request, 'post_form.html', {'form': form})



def update_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})




@cache_page(settings.CACHE_TTL)
def post_list(request):
    # Check if the data is in cache
    cached_data = cache.get('blog_list_data')
    if cached_data is not None:
        return cached_data

    # If not in cache, retrieve and cache the data
    posts = BlogPost.objects.all()
    response= render(request, 'post_list.html', {'posts': posts})
    cache.set('blog_list_data', response, settings.CACHE_TTL)
    return response



def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})





def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})