from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from . import forms
from .session import SessionOrder

def index(request):
    '''セルフオーダーのトップ画面'''
    form = forms.TableNoForm(request.POST or None)
    if form.is_valid():
        table_no = form.cleaned_data['table_no']
        # セッションデータ作成
        session_order = SessionOrder(table_no=table_no)
        request.session['session_order'] = session_order.as_dict()
        # メニュー画面へリダイレクトする
        return redirect('menu')
    return render(request, 'index.html', {'form': form})

class MenuView(TemplateView):
    '''メニュー画面'''
    template_name = 'menu.html'
