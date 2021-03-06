from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Article
from .forms import ArticleForm, ArticleUpdateForm

# Create your views here.

@login_required
def article_create_view(request):
  form = ArticleForm(request.POST or None)
  context = {
    'form': form,
    'status': 'create',
  }
  if form.is_valid():
    article_object = form.save(commit=False)
    article_object.user = request.user
    article_object.save()
    # context['form'] = ArticleForm()
    # context['object'] = article_object
    # context['created'] = True
    # return redirect('articles:detail', slug=article_object.slug)
    return redirect(article_object.get_absolute_url())
  return render(request, 'articles/create.html', context = context)

@login_required
def article_update_view(request, slug):
  obj = get_object_or_404(Article, slug=slug, user=request.user)
  form = ArticleUpdateForm(request.POST or None, instance=obj)
  context = {
    'form': form,
    'status': 'update',
  }
  if form.is_valid():
    form.save()
    return redirect(obj.get_absolute_url())
  return render(request, 'articles/create.html', context=context)


@login_required
def article_delete_view(request, slug=None):
  obj = get_object_or_404(Article, slug=slug, user=request.user)
  if request.method == "POST":
    obj.delete()
    return redirect('articles:all-user-articles')
  context = {
    "object": obj
  }
  return render(request, "articles/delete.html", context)


def article_detail_view(request, slug=None):
  article_obj = None
  if slug is not None:
    try:
      article_obj = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
      raise Http404
    except Article.MultipleObjectsReturned:
      article_obj = Article.objects.filter(slug=slug).first()
    except:
      raise Http404
  context = {
    'object': article_obj
  }
  return render(request, 'articles/article_detail_view.html', context = context)

@login_required
def all_articles_user_view(request):
  if request.user.is_authenticated:
    articles_obj = Article.objects.filter(user=request.user)
  else:
    raise Http404
  context = {
    'object_list': articles_obj
  }
  return render(request, 'articles/all_articles_user.html', context = context)