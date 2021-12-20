# I have created this file....

from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#    return HttpResponse('''<h1>hello karan bhai</h1> <a href="https://www.youtube.com/">Youtube</a>
#     <a href="https://www.twitter.com/">Twiter</a>
#     <a href="https://www.instagram.com/">Instagram</a>
#     <a href="https://www.facebook.com/">Facebook</a>''')

# def about(request):
#    return HttpResponse("about karan bhai")


def index(request):
    # params = {'name': 'karan', 'place': 'mohali'}
    # return render(request, 'index.html',params)
    return render(request, 'index.html', )
    # return HttpResponse('''<h1>Home </h1>
    # <a href="http://127.0.0.1:8000/removepunc"> Remove Punch</a><br>
    # <a href="http://127.0.0.1:8000/capfirst">Capatilize First</a><br>
    # <a href="http://127.0.0.1:8000/newlineremover">NewLine Remover</a><br>
    # <a href="http://127.0.0.1:8000/spaceremover">Space Remover</a><br>
    # <a href="http://127.0.0.1:8000/charcount">Character Counter</a>''')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    #Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which Checkbox is on
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = 0
        for char in djtext:
            if char == " ":
                pass
            else:
                analyzed = analyzed + 1
        params = {'purpose': 'Counting Characters', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse("Error")
        #return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)
# def removepunc(request):
#    djtext = request.GET.get('text', 'default')
#    print(djtext)
#    return HttpResponse('''<a href="/"> BACK <a/><br>Remove Punch''')


# def capfirst(request):
#    return HttpResponse('''<a href="/"> BACK <a/><br> Capaitaize first''')


# def newlineremover(request):
#    return HttpResponse('''<a href="/"> BACK <a/> <br> newline remover''')


# def spaceremover(request):
#    return HttpResponse('''<a href="/"> BACK <a/> <br> space remover''')


# def charcount(request):
#    return HttpResponse('''<a href="/"> BACK <a/> <br> character remover''')
