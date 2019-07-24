from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Halaman_Home'),
    path('blog/',views.Blogs, name='Halaman_Blog'),
    path('mentee/',views.Mentees, name='Halaman_Mentee'),
    path('mentor/',views.Mentors, name='Halaman_Mentor'),
    path('author/',views.Author, name='Halaman_Author'),
    path('inputmentee/',views.listmentee, name='Daftar_Mentee'),
    path('inputmentor/',views.listmentor, name='Daftar_Mentor'),
    path('inputblog/',views.listblog, name='Daftar_Author'),
]
