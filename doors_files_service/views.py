import doors_files_service.localsettings as settings
from .forms import DoorsImagesForm
from .models import DoorsImages
import hashlib
import os

LIMIT_PER_DIR = 1000


def upload_file(request):
    if request.method == 'POST':
        if request.POST.get('type', None) == 'marketplace':
            src_file_name = request.POST.get('src', None)
            if src_file_name and src_file_name.startswith(settings.MEDIA_URL):
                src_file_name = src_file_name[len(settings.MEDIA_URL):]

            if src_file_name:
                file_name = src_file_name.split('/')[-1:][0]
            else:
                file_name = request.FILES['file'].name
                file_ending = file_name.split('.')[-1]
                file_name = unicode(request.POST.get('id', '0')) + u"_" + u"".join(file_name.split('.')[:1])
                file_name = ".".join((hashlib.sha1(file_name).hexdigest(), file_ending))

            file_subpath = os.path.join(
                request.POST.get('type', 'undefined'),
                request.POST.get('object', 'undefined'),
                str(int(request.POST.get('id', '0'))/LIMIT_PER_DIR),
                request.POST.get('id', '0'))
            full_path = os.path.join(settings.MEDIA_ROOT, file_subpath)
            if not os.path.exists(full_path):
                os.system("mkdir -p %s" % full_path)

            destination = open(os.path.join(full_path, file_name), "wb+")
            if src_file_name:
                source = open(os.path.join(settings.MEDIA_ROOT, src_file_name), "rb")
                destination.write(source.read())
            else:
                destination.write(request.FILES['file'].file.read())
            destination.close()

            new_file = DoorsImages()
            new_file.image = os.path.join(file_subpath, file_name)
            new_file.save(add_watermark=True)
            return JsonResponse({'msg': 'ok', 'path': new_file.image.url})
    else:
        return JsonResponse({'msg': 'bad method'})

