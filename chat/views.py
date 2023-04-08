from django.shortcuts import render


def startpage(request):
    return render(request, 'chat/startpage.html')