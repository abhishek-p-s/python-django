from django.urls import path
from watchlist_app.api.views import  watch_list,watch_details, stream_platform, stream_platform_details

urlpatterns = [
    path('list/', watch_list, name='movie-list'),
    path('<int:id>/', watch_details, name='movie-details'),
    path('stream/', stream_platform, name='stream-platform'),
    path('stream/<int:id>/', stream_platform_details, name='stream-details')
]
