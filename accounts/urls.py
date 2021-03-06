from django.conf.urls import url, include
from accounts.views import (logout, login, registration, update_profile,
                            provider_profile, user_profile)
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^update_profile/$', update_profile, name="update_profile"),
    url(r'^provider_profile/(?P<pk>\d+)', provider_profile,
        name="provider_profile"),
]
