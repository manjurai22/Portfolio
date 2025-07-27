from django.urls import path
from portfolio_app import views
urlpatterns=[
    path("",views.portfolio,name="portfolio"),
    path("project/",views.project_list, name="project-list"),
    path("project-create/",views.project_list,name="project-create"),
]