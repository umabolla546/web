from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings
import logging
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPostForm
from .models import BlogPost

CACHE_TTL=getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)

logger = logging.getLogger('info_logger')

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                logger.info("New blog post created: %s", form.cleaned_data['title'])
                return redirect('post_list')
            except Exception as e:
                logger.error("Error creating new blog post: %s", str(e))
        else:
            logger.warning("Invalid form data submitted")
    else:
        form = BlogPostForm()

    return render(request, 'post_form.html', {'form': form})

def update_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            try:
                form.save()
                logger.info("Blog post updated: %s", post.title)
                return redirect('post_list')
            except Exception as e:
                logger.error("Error updating blog post: %s", str(e))
        else:
            logger.warning("Invalid form data submitted for post update")
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'post_form.html', {'form': form})

def post_detail(request, pk):
    try:
        post = cache.get(f'post_{pk}')  # Use a unique key for each post
        print('data from cache')

        if not post:
            post = get_object_or_404(BlogPost, pk=pk)
            cache.set(f'post_{pk}', post)

        logger.info("Accessed post detail view for post with ID %s", pk)

        return render(request, 'post_detail.html', {'post': post})
    except Exception as e:
        logger.error("Error accessing post detail view: %s", str(e))

def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        try:
            # Log the deletion of the post
            logger.info("Deleted post with ID %s: %s", pk, post.title)

            post.delete()
            return redirect('post_list')
        except Exception as e:
            logger.error("Error deleting blog post: %s", str(e))
    return render(request, 'post_confirm_delete.html', {'post': post})




# @cache_page(settings.CACHE_TTL)
# # def post_list(request):
# #     posts = BlogPost.objects.all()
# #     return render(request, 'post_list.html', {'posts': posts})

@cache_page(settings.CACHE_TTL)
def post_list(request):
    try:
        # Fetch the list of blog posts from the database
        posts = BlogPost.objects.all()
        # Render the template with the list of posts
        return render(request, 'post_list.html', {'posts': posts})

    except Exception as e:
        # Log the exception
        logger.error(f"An error occurred: {str(e)}")

        # For example, you can render an error page or return an error response.
        return render(request, 'error_page.html', {'error_message': 'An error occurred. Please try again later.'})
