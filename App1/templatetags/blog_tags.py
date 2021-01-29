from django import template

from ..models import Post


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest(count=5):
    latest = Post.objects.order_by('-publish')[:count]
    return {'latest': latest}
