from django.urls import path, include
from .views import index, post, blog, post_create, addauthor, search
from allauth.account.views import LoginView, LogoutView, SignupView


appname = 'Posts'
urlpatterns = [
    path('', index, name="index"),
    path('blog/', blog, name="blog"),
    path('posts/<int:id>/', post, name='post'),
    path('search', search, name="search"),
    path('post_create/', post_create, name="post_create"),
    path('accounts/login/', LoginView.as_view(template_name="log_in.html",
                                                success_url = "/"), name="login"),
    path('accounts/logout/', LogoutView.as_view(template_name="log_out.html"), name="logout"),
    path('accounts/signup/', SignupView.as_view(template_name="sign_up.html"), name="signup"),
    path('accounts/', include('allauth.urls')),
    ]
    # path('accounts/login/', auth_views.LoginView.as_view(template_name="log_in.html")),
    # path('accounts/logout/', LogoutView.as_view()),
    # path('accounts/signup/', Signup, name="signup"),
    # path('addauthor/', addauthor, name="addauthor"),
    # path('accounts/', include('django.contrib.auth.urls')),


# . accounts/login/ [name='login']
# . accounts/logout/ [name='logout']
# . accounts/password_change/ [name='password_change']
# . accounts/password_change/done/ [name='password_change_done']
# . accounts/password_reset/ [name='password_reset']
# . accounts/password_reset/done/ [name='password_reset_done']
# . accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# . accounts/reset/done/ [name='password_reset_complete']