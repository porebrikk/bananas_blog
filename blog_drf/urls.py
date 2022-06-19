"""blog_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {
      'next_page': settings.LOGOUT_REDIRECT_URL
    }, name='signout'),

    #Blog
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.PostView.as_view(), name='post'),
    path('contact/', views.FeedBackView.as_view(), name='contact'),
    path('contact/thanks/', views.thanks, name='thanks'),
    path('search', views.SearchView.as_view(), name='search'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('tag/<name>/', views.TagView.as_view(), name='tag'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
