from django.shortcuts import render

def index(request):
    '''セルフオーダーのトップページ'''
    return render(request, 'index.html')
