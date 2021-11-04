from django.urls import path
from myapp.views import hello
from django.urls import path, include
from myapp.views import goodbye

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
    path('<str:name>', hello, name='hello_name'),
    path('goodbye/', goodbye, name='goodbye_name'),
    path('goodbye/<str:name>', goodbye, name='goodbye'),
    path('<str:name>', goodbye, name='goodbye_name'),
# 
]