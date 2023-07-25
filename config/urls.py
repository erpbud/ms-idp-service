from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include
# from users.views.user_primary_views import protected_view

schema_view = get_schema_view(
   openapi.Info(
      title="MS IDP API",
      default_version='v1',
      description="Identity Service Provider APIs",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('sso/admin/', admin.site.urls),
    # path('sso/', protected_view, name='protected_view'),
    path('sso/auth/', jwt_views.TokenObtainPairView.as_view(), name='authentication'),
    path('sso/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='authentication_refresh'),
    path('sso/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('sso/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('sso/', include('users.urls'), name='users'),
]
