#Created By Us Manually!
from django.http import HttpResponse
from django.shortcuts import render, redirect

# def index(request):
#     Ex1: display the contents of a file in the same directory on the webpage
#     f = open("mysite/my.txt", "r")
#     content = f.read()
#     f.close()
#     return HttpResponse(content)
#     return HttpResponse("Sample Text") 

# def about(request):
#     Ex2: Personal Navigator
#     return HttpResponse('''<a href="https://www.youtube.com/watch?v=weAUmhABjBc&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=3">Django Playlist</a><br>''')

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    flag=False

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        flag=True
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps=="on":
        flag=True
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover=="on":
        flag=True
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        flag=True
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if (charcount == "on"):
        flag=True
        c=0
        for char in djtext:
            if char != " ":
                c=c+1

        params = {'purpose':'Character Count', 'analyzed_text':djtext+" : "+str(c)}
        return render(request, 'analyze.html', params)
    
    if flag==False:
        return HttpResponse("Choose any Option Please!")
    else:
        return render(request, 'analyze.html', params)