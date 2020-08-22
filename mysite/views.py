from django.shortcuts import render
from read.utils import get_week_read_data
from django.contrib.contenttypes.models import ContentType
from blog.models import Blog


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_week_read_data(blog_content_type)

    context={}
    context['dates'] = dates
    context['read_nums'] = read_nums
    return render(request, 'home.html', context)


