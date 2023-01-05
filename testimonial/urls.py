#Import from the core django
from django.urls import path
#Import from local app/library
from testimonial import views

urlpatterns = [
    #login
    path('', views.user_login, name='login'),
    #index
    path('index', views.index, name='index'),

    #testimonial
    path('testimonial',views.testimonial_view,name='view'),
    path('create',views.add_new,name='add.new'),
    path('update/<int:pk>',views.testimonial_update,name='testimonial.update'),
    path('delete/<int:pk>',views.testimonial_delete,name='testimonial.delete'),

    #logout
    path('logout', views.logout_user, name='logout'),

    path('search', views.search, name='search'),
]