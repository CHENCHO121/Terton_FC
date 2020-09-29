from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('academy',views.academy,name='academy'),
    path('admin_home',views.admin_dashboard,name='admin_home'),
    path('about', views.aboutUs, name='about'),
    path('contact', views.contact, name='contact'),
    path('scholarship_form', views.scholarship, name='scholarship_form'),
    path('view_scholarship',views.view_scholarship,name="view_scholarship"),
    path('delete_scholarship/<int:pk>',views.delete_scholarship,name="delete_scholarship"),
    path('self_training', views.self_Training, name='self_training'),
    path('view_SelfPaidTraining',views.view_SelfPaidTraining,name='view_SelfPaidTraining'),
    path('delete_SelfPaid/<int:pk>',views.delete_SelfPaid,name='delete_SelfPaid'),
    path('old_age_home',views.charity,name="old_age_home"),
    path('orphanage',views.orphange,name='orphanage'),
    path('financial',views.financialcrisis, name='financial'),
    path('galleryshow',views.galleryshow,name='galleryshow'),
    path('gallery',views.gallery,name='gallery'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('logout_admin',views.logout_admin,name='logout_admin'),
    path('gallery',views.gallery,name='gallery'),
    path('upload_gallery_orphane',views.upload_gallery_orphane,name='upload_gallery_orphane'),
    path('upload_gallery_football_player',views.upload_gallery_football_player,name='upload_gallery_football_player'),
    path('upload_gallery_old_age',views.upload_gallery_old_age,name='upload_gallery_old_age'),
    path('view_enquiry',views.view_enquiry, name='view_enquiry'),
    path('delete_enquiry/<int:pk>',views.delete_enquiry,name="delete_enquiry"),
    path('view_financial_crisis',views.view_financial_crisis,name='view_financial_crisis'),
    path('delete_financial_crisis/<int:pk>',views.delete_financial_crisis,name="delete_financial_crisis"),
    path('add_Old_Age',views.add_Old_Age,name='add_Old_Age'),
    path('add_orphanage',views.add_orphanage, name='add_orphanage'),
    path('view_orphanage',views.view_orphanage,name='view_orphanage'),
    path('delete_orphanage/<int:pk>',views.delete_orphanage,name='delete_orphanage'),
    path('view_old_age',views.view_old_age,name='view_old_age'),
    path('delete_old_age/<int:pk>',views.delete_old_age,name='delete_old_age'),
    path('update_orphanage/<int:pk>',views.edit_orphanage,name='update_orphanage'),
    path('update_old_age/<int:pk>',views.edit_old_age,name='update_old_age'),
    path('add_event',views.add_event,name='add_event'),
    path('view_event', views.view_event, name='view_event'),
    path('delete_event/<int:pk>', views.delete_event, name='delete_event'),
    path('update_event/<int:pk>', views.edit_event, name='update_event'),
    path('view_gallery',views.view_gallery, name='view_gallery'),
    path('delete_gallery/<int:pk>',views.delete_gallery,name='delete_gallery'),
    path('delete_gallery1/<int:pk>',views.delete_gallery1,name='delete_gallery1'),
    path('delete_gallery2/<int:pk>',views.delete_gallery2,name='delete_gallery2'),
    path('add_course',views.add_course,name="add_course"),
    path('view_course',views.view_course,name="view_course"),
    path('delete_course/<int:pk>',views.delete_course,name="delete_course"),
    path('update_course/<int:pk>',views.edit_course,name="update_course"),
    path('add_academy_detail',views.add_academy_detail,name='add_academy_detail'),
    path('view_academy_detail',views.view_academy_detail,name='view_academy_detail'),
    path('delete_academy_detail/<int:pk>',views.delete_academy_detail,name='delete_academy_detail'),


]
