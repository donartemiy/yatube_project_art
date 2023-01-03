# По умолчанию в проект Django подключена система администрирования
from django.contrib import admin
# Функция include позволит использовать path() из других файлов.
from django.urls import include, path

urlpatterns = [
    # Если на сервер пришел запрос '', только для namespace 'posts'
    # перейди в urls приложения posts и проверь там все path()
    # на совпадения с запрошенный url
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),

    # Все адреса с префиксом auth/ будут перенаправлены
    # в приложение users файл users/urls,
    # и там уже указывать auth/ в ссылке не нужно
    path('auth/', include('users.urls')),

    # Все что не проматчилось выше в  'users/urls'
    # попадет в django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')),

    path('about/', include('about.urls', namespace='about_namespace')),
]
