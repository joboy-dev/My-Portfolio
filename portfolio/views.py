from django.shortcuts import render
from django.views import View

from datetime import datetime

context = {
     'year': datetime.now().year
}

class HomeView(View):
    '''View for home page'''
    
    def get(self, request):
        return render(request, 'index.html', context)
