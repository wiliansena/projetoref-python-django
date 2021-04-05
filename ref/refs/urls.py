from django.urls import path

from . import views

urlpatterns = [
    path('', views.refList, name='ref-list'),
    path('ref/<int:id>', views.refView, name='ref-view'),
    path('newref/', views.newRef, name='new-ref'),
    path('edit/<int:id>', views.editRef, name='edit-ref'),
    path('delete/<int:id>', views.deleteRef, name='delete-ref'),
    path('colors/', views.colorList, name='colors-list'),
    path('colors/newcolor/', views.newColor, name='new-color'),
    path('colors/edit/<int:id>', views.editColor, name='edit-color'),
    path('colors/delete/<int:id>', views.deleteColor, name='delete-color'),
]