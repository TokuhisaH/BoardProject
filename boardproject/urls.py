from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#画像がアップロードされるたびにURLを追加する必要があるので+staticでその処理を行う
#MEDIA_URLで画像の管理、STATIC_URLでは静的ファイル（CSSとか）の管理
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('boardapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
