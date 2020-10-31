# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("""
    # <h1>Home</h1>
    # <button><a href="http://127.0.0.1:8000/rempunc">Remove Punc</a></button>
    # <button><a href="http://127.0.0.1:8000/capfirst">Capitalize First</a></button>
    # <button><a href="http://127.0.0.1:8000/newlineremove">New Line Remove</a></button>
    # <button><a href="http://127.0.0.1:8000/charcount">Char Count</a></button>

    # """) 

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('rempunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    if(charcount=='on'):
        count = 0
        for char in djtext:
            count += 1 
        

    elif removepunc == 'on':
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed


    elif(fullcaps=='on'):
        analyzed= ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed

    elif(newlineremover=="on"):
        analyzed = ''
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        djtext = analyzed

    elif(extraspaceremover=='on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==' '):
                analyzed = analyzed + char         
        djtext = analyzed      
        
    else: 
        return HttpResponse("Error")
    params = {'analyzed_text': djtext}
    return render(request, 'analyze.html', params)

def capitalizefirst(request):
    return HttpResponse("<a href='/'>Back</a>")

def newlineremove(request):
    return HttpResponse("<a href='/'>Back</a>")

def spaceremover(request):
    return HttpResponse("<a href='/'>Back</a>")

def charcount(request):
    return HttpResponse("<a href='/'>Back</a>")

