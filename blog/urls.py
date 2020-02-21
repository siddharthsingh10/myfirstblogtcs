certifi==2019.11.28
chardet==3.0.4
docopt==0.6.2
idna==2.9
python-dateutil==2.8.1
pythonanywhere==0.8.3
requests==2.23.0
six==1.14.0
urllib3==1.25.8

from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list,name=post_list),
    ]
