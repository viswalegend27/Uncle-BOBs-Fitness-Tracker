def build_diet_prompt(data):
    return f"""
    Create a {data['diet_type']} Indian diet plan for a goal of {data['goal']}.
    Target: {data['weight_goals'][0]} calories.

    Return ONLY a JSON object with this structure:
    {{
    "meals": {{
        "breakfast": {{"title": "", "items": [], "kcal": 0}},
        "lunch": {{"title": "", "items": [], "kcal": 0}},
        "snacks": {{"title": "", "items": [], "kcal": 0}},
        "dinner": {{"title": "", "items": [], "kcal": 0}}
    }},
    "total_kcal": 0
    }}
    Do not include any pre-amble or post-amble text.
    """
