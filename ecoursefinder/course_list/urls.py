from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # Your existing URL patterns
    path('',views.course_list,name='course_list'),
    path('home/',views.under_construction,name='home'),
    path('about/',views.under_construction,name='about'),
    path('teacher/',views.under_construction,name='teacher'),
    path('blog/',views.under_construction,name='blog'),
    path('contact/',views.under_construction,name='contact'),
    path('under_construction/',views.under_construction,name='under_construction')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


