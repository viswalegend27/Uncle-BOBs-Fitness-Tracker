import json
import re
from google import genai
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .forms import CalorieCalculatorForm, DietPlannerForm
from .prompts.diets_prompt import build_diet_prompt
from .services import height_conversion, lbs_to_kg, calculate_bmr, get_weightGoals
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["trainer_bob"]


def home_view(request):
    return render(request, "home.html")


def exercises_view(request):
    return render(request, "exercises.html")


def muscle_detail_view(request, muscle_name):
    exe_collection = db["exercises_detail"]
    document = exe_collection.find_one({"category": muscle_name.lower()})
    cont = []

    if document:
        # contains actual exercise data
        exercise_list = document.get("exercises", [])
        # contains catgory
        display_name = document.get("category", muscle_name).capitalize()
    else:
        exercise_list = []
        display_name = muscle_name.capitalize()

    cont = {"name": display_name, "exercises": exercise_list}
    return render(request, "muscle-detail.html", cont)


def diet_blog_view(request):
    blog_collection = db["exercise_blogs"]

    blogs = list(blog_collection.find({}))
    cal_def_data = [
        blog.get("content") for blog in blogs if blog.get("type") == "caloric_deficit"
    ]

    cal_surp_data = [
        blog.get("content") for blog in blogs if blog.get("type") == "caloric_surplus"
    ]

    return render(
        request, "diet-blogs.html", {"cal_def": cal_def_data, "cal_surp": cal_surp_data}
    )


def calori_calc_view(request):
    form = CalorieCalculatorForm(request.POST or None)
    m_cal = None
    cal_bmr = None

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        weight = data["weight"]
        units = data["unit_system"]
        h_cm = data["height_cm"]
        h_ft = data["height_ft"]
        h_in = data["height_in"]
        age = data["age"]
        gender = data["gender"]
        activity = data["activity"]

        if h_cm:
            height = h_cm
        elif h_ft and h_in:
            height = height_conversion(h_ft, h_in)
        else:
            height = 0

        if units == "imperial":
            weight_kg = lbs_to_kg(weight)
        else:
            weight_kg = weight

        bmr = calculate_bmr(weight_kg, height, age, gender)

        match activity:
            case "bmr":
                cal_bmr = bmr
            case "sedentary":
                m_cal = get_weightGoals(bmr, activity)
            case "light-exercises":
                m_cal = get_weightGoals(bmr, activity)
            case "moderate-exercises":
                m_cal = get_weightGoals(bmr, activity)
            case "active-exercises":
                m_cal = get_weightGoals(bmr, activity)
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse(
                {
                    "success": True,
                    "bmr": cal_bmr,
                    "m_goals": m_cal,
                }
            )

    return render(
        request,
        "calorie-calc.html",
        {
            "form": form,
            "m_goals": m_cal if m_cal else None,
            "bmr": cal_bmr if cal_bmr else None,
        },
    )


def diet_planner_view(request):
    diet_form = DietPlannerForm(request.POST or None)
    # introducing my form to my context var.
    diet_data = None

    if request.method == "POST" and diet_form.is_valid():
        data = diet_form.cleaned_data
        prompt = build_diet_prompt(data)
        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=prompt,
            config={"max_output_tokens": 500},
        )

        try:
            # Clean Markdown formatting.
            raw_text = response.text
            clean_json = re.sub(
                r"^```json\s*|```$", "", raw_text, flags=re.MULTILINE
            ).strip()
            diet_data = json.loads(clean_json)
        except (json.JSONDecodeError, AttributeError):
            # Fallback in case of an error
            diet_data = {
                "error": "Could not generate a structured plan. Please try again."
            }

    # Combine everything into the context
    context = {"form": diet_form, "diet_data": diet_data}

    return render(request, "diet-planner.html", context)
