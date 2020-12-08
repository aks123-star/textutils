# i have created this file- akanksha

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'akanksha', 'place':'banda'}
    return render(request, 'index.html')

def capitalizefirst(request):
    return HttpResponse('''this is capitalizefirst 
                        <br> 
                        <a href="/">back to home</a>''')

def newlineremove(request):
    return HttpResponse("this is newlineremove")

def spaceremove(request):
    return HttpResponse("this is spaceremove")

def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    # print(djtext)

#get the values of checkbox
    removepunc = request.GET.get('removepunc', 'off')
    caps = request.GET.get('caps', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

#check which checkbox value is on

    if removepunc== "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {"purpose":"removing punctuation", "analyzed_text":analyzed}
        return render(request, 'analyze.html', params)

    elif caps == "on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params = {"purpose":"capitalizing all letters", "analyzed_text":analyzed}
        return render(request,'analyze.html', params)

    elif newlineremove == "on":
        analyzed=""
        for char in djtext:
            if char is not "/n":
                analyzed = analyzed+char

        params = {"purpose":"removing new line", "analyzed_text":analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == "on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char

        params = {"purpose": "removing extra space", "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)

    elif charcount == "on":
        count=0
        for char in djtext:
            if not char == " ":
                count=count+1

        params = {"purpose": "removed extra space", "analyzed_text": count}
        return render(request, 'analyze.html', params)

    else :
        return HttpResponse("Please keep your inputs valid!")

def charcount(request):
    return HttpResponse("this is charcount")