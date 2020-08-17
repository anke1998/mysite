from django.contrib.contenttypes.models import ContentType
from .models import Readnum

def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" %(ct.model, obj.pk)

    if not request.COOKIES.get(key):
        if Readnum.objects.filter(content_type=ct, object_id=obj.pk).count():
            readnum = Readnum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            readnum = Readnum(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()
    return key
