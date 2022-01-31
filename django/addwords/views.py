from django.shortcuts import render
import requests
# Create your views here.
def add_word(request):
    if (request.method == 'POST'):
            r = requests.post(' http://localhost:8080/add/'+ request.POST['word']+'/'+request.POST['definition'])
            if (r.status_code == 200):
                context = {"msg":"Word entered succesfully"}
                return render(request,'message.html', context)
            else:
                print(r,r.status_code)
                context = {"msg":"Server error"}
                return render(request,'message.html', context)
    return render(request, 'login.html')
    