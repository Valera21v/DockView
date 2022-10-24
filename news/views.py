from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category, Marker
from django.contrib.auth.decorators import login_required, permission_required
from .forms import NewsForm, CategoryForm, NewsUpdateForm


@login_required
@permission_required('news.view_news')
def index(request):
    if request.user.groups.filter(name='Обычный пользователь').exists() == True:
        news_users = Marker.objects.filter(id_user=request.user)
        news_user_marker = news_users.filter(
            marker=True)  # <QuerySet [<Marker: Marker object (1)>, <Marker: Marker object (6)>, <Marker: Marker object (7)>]>
        news_user_id = []
        for id_news in news_user_marker:
            news_id = id_news.id_news  # тут получил имя каждой новости
            news_user_id.append(news_id)
        news = news_user_id
        news = News.objects.exclude(title__in=news)
        context = {
            'news': news,
            'title': 'Список новостей',
        }
        return render(request, template_name='news/index.html', context=context)
    else:
        news = News.objects.all()
        user_all_group = []
        d = []
        info_dont_marker = []
        users_all = User.objects.filter(groups__name='Обычный пользователь')

        for i in users_all:  # Создаю список обычных пользователей
            us = (i.last_name + " " + i.first_name)
            user_all_group.append(us)

        for item in news:
            news_pk = item.pk
            marker = Marker.objects.filter(id_news_id=news_pk)
            news_user_marker = []

            for id_user in marker:
                user_id_news = id_user.id_user
                news_user_marker.append(user_id_news.last_name + " " + user_id_news.first_name)

            user_dont_marker = list(set(user_all_group) ^ set(news_user_marker))

            if user_dont_marker == []:
                user_dont_marker = ["Все ознакомились!"]

            if news_user_marker == []:
                news_user_marker = ["Никто не ознакомился!"]
                # info = dict({item: (dict({tuple(news_user_marker): info_dont_marker}))})
                info = dict({item: (dict({tuple(news_user_marker): user_dont_marker}))})
            else:
                # info = dict({item: (dict({tuple(news_user_marker): info_dont_marker}))})
                info = dict({item: (dict({tuple(news_user_marker): user_dont_marker}))})

            d.append(info)

        context = {
            'news': d,
        }
    return render(request, template_name='news/big_boss_panel.html', context=context)


@login_required
@permission_required('news.view_news')
def get_category(request, category_id):
    news_users = Marker.objects.filter(id_user=request.user)
    news_user_marker = news_users.filter(
        marker=True)
    news_user_id = []
    for id_news in news_user_marker:
        news_id = id_news.id_news  # тут получил имя каждой новости
        news_user_id.append(news_id)
    news = news_user_id
    news = News.objects.exclude(title__in=news)
    news = news.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


@login_required
@permission_required('news.view_news')
def get_category_archive(request, category_id):
    news_users = Marker.objects.filter(id_user=request.user)
    news_user_marker = news_users.filter(
        marker=True)

    news_user_id = []
    for id_news in news_user_marker:
        news_id = id_news.id_news  # тут получил имя каждой новости
        news_user_id.append(news_id)

    category = Category.objects.get(pk=category_id)
    news = News.objects.filter(title__in=news_user_id)
    news = news.filter(category_id=category_id)

    return render(request, 'news/category_archive.html', {'news': news, 'category': category})


@login_required
@permission_required('news.view_news')
def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)

    return render(request, 'news/view_news.html', {"news_item": news_item})


@login_required
@permission_required('news.view_news')
def btn_marker(request, news_id):
    Marker.objects.create(id_user=request.user, id_news=News.objects.get(pk=news_id), marker=True)
    get_object_or_404(News, pk=news_id)
    return redirect('home')


@login_required
@permission_required('news.view_news')
def archive(request):
    news_users = Marker.objects.filter(id_user=request.user)
    news_user_marker = news_users.filter(
        marker=True)
    news_user_id = []
    for id_news in news_user_marker:
        news_id = id_news.id_news  # тут получил имя каждой новости
        news_user_id.append(news_id)
    news = news_user_id
    item = News.objects.filter(title__in=news)
    return render(request, template_name='news/archive.html', context={'news': item})


@login_required
@permission_required('news.view_news')
def view_news_archive(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)

    return render(request, 'news/view_news_archive.html', {"news_item": news_item})


@login_required
@permission_required('news.change_news')
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()

    if request.method == 'POST':
        form_cat = CategoryForm(request.POST, request.FILES)
        if form_cat.is_valid():
            form_cat.save()
            return redirect('add_news')
    else:
        form_cat = CategoryForm()

    return render(request, 'news/add_news.html', {'form': form, 'form_cat': form_cat})


@login_required
@permission_required('news.view_news')
def updated_news(request, pk):
    news_up = News.objects.get(pk=pk)
    template_name = 'news/updated_news.html'

    if request.method == 'POST':
        form = NewsUpdateForm(request.POST, request.FILES, instance=news_up)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        NewsUpdateForm()
    context = {
        'news_up': news_up,
        'form': NewsUpdateForm(instance=news_up),
    }
    return render(request, template_name, context)



@login_required
@permission_required('news.view_news')
def delete_news(request, pk):
    news_up = News.objects.get(pk=pk)
    news_up.delete()
    return redirect('home')
