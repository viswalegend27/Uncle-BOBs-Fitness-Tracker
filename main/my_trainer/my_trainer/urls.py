from django.contrib import admin
from django.urls import path
from trainer_bob.views import (
    home_view,
    exercises_view,
    muscle_detail_view,
    diet_blog_view,
    calori_calc_view,
    diet_planner_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("exercises/", exercises_view, name="exercises"),
    path("exercises/<str:muscle_name>", muscle_detail_view, name="muscle_detail"),
    path("diet-blogs/", diet_blog_view, name="diet_blogs"),
    path("calorie-cal/", calori_calc_view, name="calorie-calc"),
    path("diet-planner/", diet_planner_view, name="diet-planner"),
]
