from django.urls import path
from .views import (
    subject_list,
    create_subject,
    create_subject_page,
    get,
    delete_page_subject,
    delete_subject,
    delete_page_book,
    delete_book,
    create_book,
    create_book_page,
    update_subject_page,
    update_subject,
    download,

)

app_name = 'subject'
urlpatterns = [
    path('list/', subject_list, name='list'),
    path('create_subject/', create_subject, name='create_subject'),
    path('create_subject_page/', create_subject_page, name='create_subject_page'),
    path('create_book/<int:pk>', create_book, name='create_book'),
    path('create_book_page/<int:pk>', create_book_page, name='create_book_page'),
    path('get/<int:pk>', get, name='get'),
    path('delete_page_subject/<int:pk>', delete_page_subject, name='delete_page_subject'),
    path('delete_subject/<int:pk>', delete_subject, name='delete_subject'),
    path('delete_page_book/<int:pk>', delete_page_book, name='delete_page_book'),
    path('delete_book/<int:pk>', delete_book, name='delete_book'),
    path('update_subject_page/<int:pk>', update_subject_page, name='update_subject_page'),
    path('update_subject/', update_subject, name='update_subject'),
    path('download/<str:generated_name>', download, name='download'),

]
