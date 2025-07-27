from django.urls import path
from portfolio_app import views
urlpatterns=[
    path("",views.portfolio,name="portfolio"),
    path("project/",views.project_list, name="project-list"),
    path("project-create/",views.project_list,name="project-create"),
    path("project-update/<int:pk>/",views.project_update, name="project-update"),
    path("project-list/<int:pk>/", views.project_delete, name="project-delete")
]