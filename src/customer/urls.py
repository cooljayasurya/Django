from django.conf.urls import url
from customer import views

urlpatterns = [
    url(r'^customer/$', views.customer_list),
    url(r'^customers/(?P<pk>[0-9]+)$', views.customer_detail),
    # url(r'^customer/age/(?P &lt;age&gt;[0-9]+)/$', views.customer_list_age),
]
