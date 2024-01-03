from django.urls import path
from .views import index, company_detail, start, start2, rubric_detail, add_comment

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', company_detail, name='company_detail'),
    path('start/', start, name='start'),
    path('start2/', start2, name='start2'),
    path('catalog/<str:rubric>/', rubric_detail, name='rubric_detail'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
]
