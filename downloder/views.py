import os
from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, Http404
from yt_dlp import YoutubeDL

# Create your views here.
def index(request):
    return render(request,'index.html')

#youtube
def download_youtube_video(request):

    if request.method == 'POST':
        video_url = request.POST.get('video_url')  
        if not video_url:
            return HttpResponse('Invalid URL', status=400)

        try:
            # Ensure media directory exists
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)

            # Temporary filename for the downloaded video
            temp_filename = "Rd_downloader.mp4"
            temp_file_path = os.path.join(settings.MEDIA_ROOT, temp_filename)
            
            ydl_opts = {
                'outtmpl': temp_file_path,
                'format': 'mp4',
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            # Return the downloaded video as a response
            if os.path.exists(temp_file_path):
                with open(temp_file_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type="video/mp4")
                    response['Content-Disposition'] = f'attachment; filename="Rd_downloader.mp4"'
                    return response
            else:
                return HttpResponse("Error: File not found after download.", status=500)
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}", status=500)
        finally:
            # Cleanup the temporary file
            if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
                os.remove(temp_file_path)

    return HttpResponse('Invalid Request', status=400)