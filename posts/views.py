from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Count, Q
from .models import Post, Gallery
from newsletter.models import SignUp

from .forms import CommentForm

def search(request):
    category_count = get_category_count()
    queryset = Post.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)   |
            Q(overview__icontains=query)
            #Q(author__icontains=query)
        ).distinct()

    most_recent = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'queryset': queryset,
        'most_recent': most_recent,
        'category_count': category_count,
        'query': query
    }
    return render(request, 'search_results.html', context)

def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))

    return queryset
    

def index(request):
    featured_post = Post.objects.filter(featured=True)
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    gallery = Gallery.objects.all()

    if request.method == "POST":
        email = request.POST['email']
        new_signup = SignUp()
        new_signup.email = email
        new_signup.save()

    context = {
        'most_recent': most_recent,
        'object_list': featured_post,
        'gallery': gallery
    }
    return render(request, 'index.html', context)

def blog(request):
    category_count = get_category_count()

    post_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(post_list, 6) # change later
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    most_recent = Post.objects.order_by('-timestamp')[0:3]

    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)

def post(request, title):
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    post = get_object_or_404(Post, title=title)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)#,instance=user)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'post.html', context)

def contact(request):
    return render(request, 'contact.html')

def works(request):
    return render(request, 'howworks.html')

def privacy(request):
    return render(request, 'privacy.html')