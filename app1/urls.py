from .views import index,about,contact,jewellery,login, productview, searchview,signup,logout,addpro
from django.urls import path

urlpatterns = [

    path('index/',index, name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('jewellery/',jewellery,name='jewellery'),
    path('',login,name='login'),
    path('signup/',signup,name='signup'),
    path('view/<int:abc>',productview,name='proview'),
    path('search/',searchview,name='search'),
    path('logout/',logout,name='logout'),
    path('addpro/',addpro,name='addpro')

    
]
