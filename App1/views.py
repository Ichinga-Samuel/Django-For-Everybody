from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.core.mail import send_mail

from taggit.models import Tag
from .models import Post
from .forms import EmailPostForm, CommentForm


def post_list(request, tag_slug=None):

    tag = None
    posts = objects = Post.objects.all()
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        objects = objects.filter(tags__in=[tag])

    page = request.GET.get('page')
    paginator = Paginator(objects, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts, 'page': page, 'tag': tag})


def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, slug=post,
                             status='draft',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'comments': comments,
                                                     'new_comment': new_comment,
                                                     'comment_form': comment_form})


def share_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='draft')
    sent = False
    if request.method == 'POST':
        forms = EmailPostForm(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"

            message = f"Read {post.title} at {post_url} {cd['name']}\'s comments: {cd['comments']}\n\n"

            send_mail(subject, message, 'admin@myblog.com',
                      [cd['to']])
            sent = True
    else:
        forms = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'forms': forms, 'sent': sent})


def dje(request):
    return HttpResponse('Hello, world. eef15e70 is the polls index.')


