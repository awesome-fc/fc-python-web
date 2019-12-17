# coding=utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home Django</h1>", status=200)

def signin_form(request):
    # action url 中的service_name,function_name need replace
    html = '''<form action="/signin" method="post">
         <p><input name="username"></p>
         <p><input name="password" type="password"></p>
         <p><button type="submit">Sign In</button></p>
         </form>'''

    resp = HttpResponse(html, status=200)
    return resp

@csrf_exempt
def signin(request):
    if request.POST['username'] == 'admin' and request.POST['password'] == 'password':
        html = '<h3>Hello, admin!</h3>'
    else:
        html = '<h3>Bad username or password.</h3>'
    resp = HttpResponse(html, status=200)
    return resp
