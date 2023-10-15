from django.urls import path
from . import views



urlpatterns = [
   path("", views.home_page, name="homepage"),
   path("update_task_status/<int:id>/", views.update_task_status, name="update_task_status"),
   # path("modal_view/<int:id>/", views.modal_content, name="modal_view"),
   path("delete_task/<str:id>/", views.delete_task, name="delete_task"),
   path("edit_task/<str:id>/", views.edit_task, name="edit_task"),
   path("set-theme/", views.set_theme),
   path("set_priority/<int:id>/", views.set_priority, name="set_priority"),
   path("register", views.register_user, name="register"),
   path("login", views.login_user, name="login"),
   path("logout", views.logout_user, name="logout"),
   path("add_task", views.add_task, name="add_tasks"),
   path("user_timezone/", views.user_timezone, name="user_timezone")
]



