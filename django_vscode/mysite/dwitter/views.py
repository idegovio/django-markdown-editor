import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile


def dashboard(request):
    return render(request, "./dwitter/base.html")

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "./dwitter/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)    # get the requested profile using the primary key ID number (pk), which automatically correlate to the urls.py message
    return render(request, "dwitter/profile.html", {"profile": profile})


# def hello_there(request, name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)