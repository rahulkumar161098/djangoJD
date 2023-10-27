
from django.urls import path
from leads import views


urlpatterns = [
   path('', views.home_view),
   path('<int:id>', views.lead_detail_view),
   path('create_lead', views.cerate_lead)
]
