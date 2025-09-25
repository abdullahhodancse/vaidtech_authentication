from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import time

class AutoLogout(MiddlewareMixin):
    def process_request(self,request):
        if request.user.is_authenticated:
            login_time=int(time.time())
            last_time=request.session.get('last_time',login_time)

            if login_time -last_time >5*30:
                logout(request)
                return redirect('login')
            
            request.session['last_time']=login_time