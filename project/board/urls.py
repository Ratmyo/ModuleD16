from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticlesList.as_view()),
    path('<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('response/', ResponseCreate.as_view(), name='responses_create'),
    path('responselist/', ResponseList.as_view(), name='responses'),
]
