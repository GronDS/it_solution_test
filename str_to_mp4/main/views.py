from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import  str_to_mp4_func
from .models import Videos
from .forms import VideoForm
import mimetypes

def main(request):
    videos = Videos.objects.order_by('-id')[:10]
    return render(request,'main/main.html',{"title" : "Main page", "videos": videos})

def mp4(request):
    error = ""
    if request.method == "POST":
        form = VideoForm(request.POST)
        link_value = form["word"].value()
        # imp_value = request.GET.get(VideoForm.Meta.widgets["word"])
        # print(imp_value)
        if form.is_valid():
            form.save()
            return redirect(f'/mp4/{link_value}')
        else:
            error = "Incorrect form"
    
    form = VideoForm()
    context = {'form' : form}
    return render(request,'main/mp4.html', context)

def mp4Details(request, textID):
    filename = str_to_mp4_func.make_words_move(textID)
    fl_path = f'video/{filename}'
    fl = open(fl_path, "rb")
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mp4)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response