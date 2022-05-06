from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #parameter = {'name':'vaibhav', 'gender':'male'}
    return render(request, 'index2.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    removespace = request.POST.get('removespace', 'off')
    charcount = request.POST.get('charcount', 'off')
    #print(removepunc)
    #print(djtext)

    # check which checkbox is on
    if removepunc == 'on':
        analyzed = ""
        puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in puncs:
                analyzed += char
        params = {'purpose' : 'Removed Punctuations!', 'analyzed_text': analyzed}
        #Analyze the text
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose' : 'Changed to UPPERCASE!', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if(newlineremove == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r': 
                analyzed += char
        params = {'purpose':'Removed new line','analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if(removespace == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext): #if char != '  ': 
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        params = {'purpose':'Removed extra space','analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if(charcount == 'on'):
        analyzed = len(djtext)
        params = {'purpose':'Count of characters','analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)

    if(removepunc != 'on' and fullcaps != 'on' and newlineremove != 'on' and  removespace != 'on' and charcount != 'on'):
        return HttpResponse("<h1>Error! Please select an operation</h1>")

    return render(request, 'analyze.html', params)
