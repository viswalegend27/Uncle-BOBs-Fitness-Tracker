from math import floor


def height_conversion(feet, inches):
    conv_feet = feet * 12
    conv_h = round((conv_feet + inches) * 2.54)
    return conv_h


def lbs_to_kg(lb):
    conv_kg = round(lb // 2.205, 1)
    return conv_kg


def calculate_bmr(weight, height, age, gender):
    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return round(bmr)


# -- factors that need to taken
# 87 74
# 89 78
# 90 79
# 90 81


def get_weightGoals(bmr, activity):
    m_cal = None
    weight_goals = None

    match activity:
        case "sedentary":
            m_cal = calc_maintain_cal(bmr, 1.2)
            weight_goals = w_loss_goals(m_cal, 87, 74)
        case "light-exercises":
            m_cal = calc_maintain_cal(bmr, 1.375)
            weight_goals = w_loss_goals(m_cal, 89, 78)
        case "moderate-exercises":
            m_cal = calc_maintain_cal(bmr, 1.55)
            weight_goals = w_loss_goals(m_cal, 90, 79)
        case "active-exercises":
            m_cal = calc_maintain_cal(bmr, 1.725)
            weight_goals = w_loss_goals(m_cal, 90, 81)

    goals = [m_cal, weight_goals]
    flt_goals = flattening_meList(goals)
    return flt_goals


def calc_maintain_cal(bmr, factor):
    maintainence = bmr * factor
    return floor(maintainence)


def w_loss_goals(calorie, minimum, mild):
    minimum_L = (minimum / 100) * calorie
    mild_L = (mild / 100) * calorie
    w_Loss = [floor(minimum_L), floor(mild_L)]
    return w_Loss


def flattening_meList(my_list):
    flt_list = []
    for item in my_list:
        if isinstance(item, list):
            flt_list.extend(flattening_meList(item))
        else:
            flt_list.append(item)
    return flt_list
