from django.shortcuts import render
import requests
# Create your views here.

#Function to add new words to the database
def add_word(request):
    if (request.method == 'POST'):
            r = requests.post(' http://localhost:8080/add/'+ request.POST['word']+'/'+request.POST['definition']) #Send request to add function in Flask repo
            #On success
            if (r.status_code == 200):
                context = {"msg":"Word entered succesfully"}
                return render(request,'message.html', context)
            #On failure
            else:
                print(r,r.status_code)
                context = {"msg":"Server error"}
                return render(request,'message.html', context)
    return render(request, 'login.html')
    
