from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('destination/', views.destination, name="destination"),
    path('destination/destination_single/<int:id>/', views.dSingle, name="dSingle"),
    path('blog/', views.blogs, name="blog"),
    path('blog-single/<int:blog_id>/', views.blog_single, name="blog_single"),
    path("login_view/", views.login_view, name="login_view"),
    path("register/", views.register_user, name="register_user"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout_view, name="logout"),
    path("blog/<int:blog_id>/add-comment/<int:user_id>/", views.add_Comment, name="add_Comment"),
    path("search/", views.search, name="search"),
    path("search-blog/", views.search_blog, name="search_blog"),
    path("profile/edit/email/<int:user_id>/", views.get_edit_email, name="get_edit_email"),
    path("profile/edit-email/<int:user_id>/", views.edit_email, name="edit_email"),
    path("profile/edit/username/<int:user_id>/", views.get_edit_username, name="get_edit_username"),
    path("profile/edit-username/<int:user_id>/", views.edit_username, name="edit_username"),
    path("profile/edit/password/<int:user_id>/", views.get_edit_password, name="get_edit_password"),
    path("profile/edit-email/<int:user_id>/", views.edit_password, name="edit_password"),
    path("book-tour/<int:user_id>/<int:tour_id>", views.check_out_tour, name="bookTour"),
    path("tour/<int:user_id>/", views.show_book_tour, name="check"),

    path("password_reset", auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name="password_reset"),
    path("password_reset_done", auth_views.PasswordResetView.as_view(template_name='password_reset_done.html'),
         name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>",
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("password_reset_complete",
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name="password_reset_complete"),
]
