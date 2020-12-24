from django.contrib import admin
# include module to include other files
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # home page path - nothing ''
    # including quotes urls
    path('', include('quotes.urls')),
]
