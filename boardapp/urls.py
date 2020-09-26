from django.conf.urls import url
from .views import signupfunc,loginfunc,listfunc,logoutfunc,detailfunc,goodfunc,readfunc, BoardCreate

urlpatterns = [
    url('signup/', signupfunc, name='signup'),
    url('login/', loginfunc, name='login'),
    url('list/',listfunc, name='list'),
    url('logout/', logoutfunc, name='logout'),
    url('detail/(?P<pk>\d+)',detailfunc,name='detail'),
    url('good/(?P<pk>\d+)',goodfunc,name='good'),
    url('read/(?P<pk>\d+)',readfunc,name='read'),
    url('create/',BoardCreate.as_view(), name='create'),
]
