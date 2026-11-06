from django.shortcuts import render, get_object_or_404
from .models import Blog

def fx_all_blogs(request):
    blog_count = Blog.objects.count
    t_blogs = Blog.objects.order_by('date')[:2]
    return render(request, 'blog/all_blogs.html', {'key_blogs':t_blogs, 'key_blog_count':blog_count})

def fx_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'key_blog':blog})
