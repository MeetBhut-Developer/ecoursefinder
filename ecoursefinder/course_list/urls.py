from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # Your existing URL patterns
    path('',views.index,name='index'),
    path('course/',views.course_list,name='course'),
    path('home/',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.under_construction,name='contact'),
    path('under_construction/',views.under_construction,name='under_construction'),

    # path('countdown/',views.countdown_view,name='countdown')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


