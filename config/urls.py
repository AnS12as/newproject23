from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Course Management API. Go to /api/courses/ for courses.")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
    path('', home, name='home'),
]
