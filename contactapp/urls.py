from django.conf.urls import url

from contactapp.views import ContactView

urlpatterns = [
                    url(r'^contacts/$', ContactView.as_view(), name="contact_list"),
                    url(r'^contacts/(?P<pk>[0-9]+)/$', ContactView.as_view(), name="contact_detail"),
              ]