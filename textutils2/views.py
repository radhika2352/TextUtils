from django.http import HttpResponse
from django.shortcuts import render

def index(request):
      return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    print(djtext)

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        # Analyze the Text
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        # Analyze the Text
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):  #index no. (iteration)
            if not(djtext[index] == " " and djtext[index +1] == " "):
                analyzed = analyzed + char

        # Analyze the Text
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        # Analyze the Text
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}


    if(removepunc !="on" and fullcaps !="on" and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse("Please select any Operation and Try Again !!...")


    return render(request, 'analyze.html', params)


def contact(request):
    s = '''<h2>LINKED IN PROFILE :Radhika Agrawal</h2>
        <a href="https://www.linkedin.com/in/radhikaagrawal23/">LinkedIn</a>'''
    return HttpResponse(s)

def about(request):
    return render(request, 'about.html')

