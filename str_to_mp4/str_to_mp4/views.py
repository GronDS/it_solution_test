from django.http import HttpResponse, FileResponse
from . import  str_to_mp4_func
import mimetypes

def mp4(request):
    return HttpResponse(f"<h4>Enter the text in the link after the slash</h4>")

def mp4Details(request, textID):
    filename = str_to_mp4_func.make_words_move(textID)
    fl_path = f'video/{filename}'
    fl = open(fl_path, "rb")
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mp4)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response