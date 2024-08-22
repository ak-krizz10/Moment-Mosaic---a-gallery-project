from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    
    path('',views.home,name='home'),
    
    path('signin',views.userlogin,name="signin"),
    path('signup',views.registeruser,name="signup"),
    path('signout',views.userlogout,name="signout"),
    path('createprofile',views.createprofile,name="create-profile"),
    
    
    path('Allphotos',views.allphotos,name="all"),
    path('album',views.albumns,name="album"),
    path('album/<int:id>',views.openalbumn,name="open"),
    path('favourites',views.favourites,name='fav'),
    path('image/<int:id>',views.openimage,name='image'),
    
    path('favourites/<int:id>',views.addtofavourites,name='fav-add'),
    path('favour/<int:id>',views.removefromfavourites,name='fav-remove'),
    path('delete/<int:id>',views.deleteimage,name="del"),
    
    path('upload',views.imageupload,name="upload"),
    path('profile',views.openprofile,name="profile"),
    
    
    
    path('editprofile',views.editprofile,name="edit-profile"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)