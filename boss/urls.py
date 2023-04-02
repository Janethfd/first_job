from django.urls import path
from .views import index, detail, result

app_name = "boss"

urlpatterns = [
    path('', index, name="index"),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/result/', result, name='result'),

]


# urlpatterns = [
#     path('index/', index, name="index"),
#     path('<int:pk>/', detail, name='detail'),
#     path('<int:pk>/result/', result, name='result'),

# ]
