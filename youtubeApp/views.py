from django.shortcuts import render, redirect
from pytube import *
from django.contrib import messages

# Create View
def youtube(request):
    # checking whether request.method is post or not
    if request.method == 'POST':
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        # setting video resolution
        stream = video.streams.get_highest_resolution()
        # downloads video
        stream.download()
        messages.success(request, 'Download Successfully!')
        # returning HTML page
        return render(request, 'youtube.html')
    return render(request, 'youtube.html')