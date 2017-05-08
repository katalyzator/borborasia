from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from borborasia import settings

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'main.views.index_view', name='index'),
    url(r'^about/', 'main.views.about_view', name='about'),
    url(r'^tours/', 'main.views.tours_view', name='tour'),
    url(r'^todo/', 'main.views.todo_view', name='todo'),
    url(r'^reviews/', 'main.views.review_view', name='review'),
    url(r'^regions/', 'main.views.region_view', name='region'),
    url(r'^cart/', 'main.views.get_cart', name='cart'),
    url(r'^tour/(?P<id>\d+)/$', 'main.views.single_tour', name='single_tour'),
    url(r'^add_to_cart/(?P<id>\d+)/$', 'main.views.add_to_cart', name='add_to_card'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
