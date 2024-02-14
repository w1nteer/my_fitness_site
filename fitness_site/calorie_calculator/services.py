def get_cpa(activity_level):
    CPA = {
        'минимальный': 1.2,
        'низкий': 1.375,
        'умеренный': 1.55,
        'высокий': 1.7,
        'экстремальный': 1.9
    }

    return CPA.get(activity_level)


def get_coef_by_target(target: str):
    RATES = {
        'Похудение': 0.88,
        'Поддержание': 1,
        'Набор': 1.2
    }

    return RATES.get(target)


def get_calories(gender, weight, height, age, target, activity_level):
    calories = 'Произошла ошибка. Перезагрузите страницу и введите данные еще раз, пожалуйста :)'
    cpa = get_cpa(activity_level)
    coef_by_target = get_coef_by_target(target)
    if gender == 'M':
        calories = ((66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)) * cpa) * coef_by_target
    elif gender == 'Ж':
        calories = ((655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)) * cpa) * coef_by_target

    if type(calories) in [int, float]:
        return int(calories)
    else:
        return calories