from django import forms
from .services import calculate_bmr, get_weightGoals


class CalorieCalculatorForm(forms.Form):
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    UNIT_CHOICES = [("metric", "Metric"), ("imperial", "Imperial")]
    ACTIVITY_CHOICES = [
        ("bmr", "Bmr"),
        ("sedentary", "Sedentary"),
        ("light-exercises", "Light Exercises"),
        ("moderate-exercises", "Moderate Exercises"),
        ("active-exercises", "Active Exercises"),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    unit_system = forms.ChoiceField(choices=UNIT_CHOICES)
    activity = forms.ChoiceField(choices=ACTIVITY_CHOICES)
    weight = forms.FloatField(min_value=1)
    age = forms.IntegerField(min_value=1, max_value=120)
    height_cm = forms.FloatField(min_value=1, required=False)
    height_ft = forms.IntegerField(min_value=1, required=False)
    height_in = forms.IntegerField(min_value=1, required=False)

    def clean(self):
        cleaned_data = super().clean()
        units = cleaned_data.get("unit_choices")
        h_cm = cleaned_data.get("h_cm")
        h_ft = cleaned_data.get("h_ft")
        h_in = cleaned_data.get("h_in")

        if units == "metric":
            if not h_cm:
                self.add_error("h_cm", "Please provide the height in centimeters")
        elif units == "imperial":
            if h_ft is None and h_in is None:
                err_msg = "Please provide valid units"
                if h_ft is None:
                    self.add_error("h_ft", err_msg)
                if h_in is None:
                    self.add_error("h_in", err_msg)
        return cleaned_data


class DietPlannerForm(forms.Form):
    GOAL_CHOICES = [
        ("weight-loss", "Weight Loss"),
        ("weight-gain", "Weight Gain"),
    ]
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    ACTIVITY_CHOICES = [
        ("bmr", "Bmr"),
        ("sedentary", "Sedentary"),
        ("light-exercises", "Light Exercises"),
        ("moderate-exercises", "Moderate Exercises"),
        ("active-exercises", "Active Exercises"),
    ]
    DIET_TYPE = [
        ("meat", "Meat"),
        ("vegetarien", "Vegetarien"),
        ("vegan", "Vegan"),
    ]

    # choice fields
    goal = forms.ChoiceField(choices=GOAL_CHOICES)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    activity = forms.ChoiceField(choices=ACTIVITY_CHOICES)
    diet_type = forms.ChoiceField(choices=DIET_TYPE)

    # non-choice fields
    height = forms.FloatField(min_value=1)
    weight = forms.FloatField(min_value=1)
    age = forms.IntegerField(min_value=1)

    def clean(self):
        cleaned_data = super().clean()

        height = cleaned_data.get("height")
        weight = cleaned_data.get("weight")
        age = cleaned_data.get("age")
        gender = cleaned_data.get("gender")
        activity = cleaned_data.get("activity")

        bmr = calculate_bmr(weight, height, age, gender)
        weight_goals = get_weightGoals(bmr, activity)

        if height and weight:
            bmi = weight / ((height / 100) ** 2)
            cleaned_data["bmi"] = round(bmi, 1)
            cleaned_data["bmr"] = bmr
            cleaned_data["weight_goals"] = weight_goals

            if bmi < 10 or bmi > 60:
                raise forms.ValidationError("Invalid body measurements")

        return cleaned_data
