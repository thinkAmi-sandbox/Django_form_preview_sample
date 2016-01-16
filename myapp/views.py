from formtools.preview import FormPreview
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Article
from .forms import ArticleForm

class ArticlePreviewUsingRequest(FormPreview):
    def done(self, request, cleaned_data):
        # doneの時点ではModelの保存ができていないので、
        # 自分で保存処理を実装する必要がある
        f = ArticleForm(request.POST)
        
        article = f.save(commit=False)
        article.save()
        f.save_m2m()
        
        url = reverse('ns:article-detail', args=(article.id,))
        return HttpResponseRedirect(url)


class ArticlePreviewUsingCleanedData(FormPreview):
    def done(self, request, cleaned_data):
        article = Article.objects.create(
            title = cleaned_data['title'],
            content = cleaned_data['content'],
        )
        
        article.categories.add(*cleaned_data['categories'])
    
        url = reverse('ns:article-detail', args=(article.id,))
        return HttpResponseRedirect(url)

    
class ArticleDetail(DetailView):
    model = Article