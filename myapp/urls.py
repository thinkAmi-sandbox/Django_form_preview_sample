from django.conf.urls import url
from . import views
from . import forms

urlpatterns = [
    url(r'^request/$', views.ArticlePreviewUsingRequest(forms.ArticleForm), name='article-request'),
    url(r'^cleaned_data/$', views.ArticlePreviewUsingCleanedData(forms.ArticleForm), name='article-cleaned_data'),
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view(), name='article-detail'),
]