from django.shortcuts import render
from authentication.models import User
# Create your views here.

def tablemaillog(request):
    
            user=User.objects.get(email=request.session['email'])
            logs=user.servers.get(host=request.session['server']).syslogs
            
            return render(request,"tablemaillog.html",{'logs':logs})
    