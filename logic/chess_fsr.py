from models.chess_fsr_rating_calculator import FCROutput


def _calculate_k_factor(hero_rating) -> int:
    """Определяем коэффициент K по правилам FIDE"""
    if 1000 <= hero_rating <= 1199: return 60
    elif 1200 <= hero_rating <= 1399: return 50
    elif 1400 <= hero_rating <= 1599: return 40
    elif 1600 <= hero_rating <= 1799: return 35
    elif 1800 <= hero_rating <= 1999: return 30
    elif 2000 <= hero_rating <= 2199: return 25
    elif 2200 <=hero_rating <= 2399: return 20
    elif hero_rating >= 2400: return 10
    else: raise ValueError("Рейтинг должен быть не менее 1000")



def calculate_rshf_rating(hero_rating, enemies, results):
    """
    Рассчитывает изменение рейтинга по системе РШФ

    Параметры:
    your_rating (int): ваш текущий рейтинг
    K (int): коэффициент развития
    opponent_ratings (list): список рейтингов соперников
    results (list): список результатов (1 - победа, 0.5 - ничья, 0 - поражение)

    Возвращает:
    dict: словарь с результатами расчета
    """
    # Таблица преобразования разницы рейтингов в ожидаемый результат (РШФ)
    rshf_conversion_table = [
        {"diff": [0, 3], "p": 0.50},
        {"diff": [4, 10], "p": 0.51},
        {"diff": [11, 17], "p": 0.52},
        {"diff": [18, 25], "p": 0.53},
        {"diff": [26, 32], "p": 0.54},
        {"diff": [33, 39], "p": 0.55},
        {"diff": [40, 46], "p": 0.56},
        {"diff": [47, 53], "p": 0.57},
        {"diff": [54, 61], "p": 0.58},
        {"diff": [62, 68], "p": 0.59},
        {"diff": [69, 76], "p": 0.60},
        {"diff": [77, 83], "p": 0.61},
        {"diff": [84, 91], "p": 0.62},
        {"diff": [92, 98], "p": 0.63},
        {"diff": [99, 106], "p": 0.64},
        {"diff": [107, 113], "p": 0.65},
        {"diff": [114, 121], "p": 0.66},
        {"diff": [122, 129], "p": 0.67},
        {"diff": [130, 137], "p": 0.68},
        {"diff": [138, 145], "p": 0.69},
        {"diff": [146, 153], "p": 0.70},
        {"diff": [154, 162], "p": 0.71},
        {"diff": [163, 170], "p": 0.72},
        {"diff": [171, 179], "p": 0.73},
        {"diff": [180, 188], "p": 0.74},
        {"diff": [189, 197], "p": 0.75},
        {"diff": [198, 206], "p": 0.76},
        {"diff": [207, 215], "p": 0.77},
        {"diff": [216, 225], "p": 0.78},
        {"diff": [226, 235], "p": 0.79},
        {"diff": [236, 245], "p": 0.80},
        {"diff": [246, 256], "p": 0.81},
        {"diff": [257, 267], "p": 0.82},
        {"diff": [268, 278], "p": 0.83},
        {"diff": [279, 290], "p": 0.84},
        {"diff": [291, 302], "p": 0.85},
        {"diff": [303, 315], "p": 0.86},
        {"diff": [316, 328], "p": 0.87},
        {"diff": [329, 344], "p": 0.88},
        {"diff": [345, 357], "p": 0.89},
        {"diff": [358, 374], "p": 0.90},
        {"diff": [375, 391], "p": 0.91},
        {"diff": [392, float('inf')], "p": 0.92}
    ]

    def get_expected_result(rating_diff):
        """Возвращает ожидаемый результат на основе разницы рейтингов"""
        abs_diff = abs(rating_diff)
        for item in rshf_conversion_table:
            if item["diff"][0] <= abs_diff <= item["diff"][1]:
                return item["p"] if rating_diff <= 0 else 1 - item["p"]
        return 0.5

    # Проверка входных данных
    if not enemies or len(enemies) != len(results):
        raise ValueError("Количество соперников и результатов должно совпадать")

    if hero_rating < 1000 or hero_rating > 3000:
        raise ValueError("Рейтинг должен быть в диапазоне 1000-3000")

    if any(r < 1000 or r > 3000 for r in enemies):
        raise ValueError("Рейтинги соперников должны быть в диапазоне 1000-3000")

    if any(r not in (0, 0.5, 1) for r in results):
        raise ValueError("Результаты должны быть 0, 0.5 или 1")

    # Расчет изменений
    game_changes = []
    total_score = 0.0
    total_opponent_rating = 0
    K = _calculate_k_factor(hero_rating)
    for opp_rating, result in zip(enemies, results):
        rating_diff = opp_rating - hero_rating
        expected = get_expected_result(rating_diff)
        change = K * (result - expected)

        game_changes.append(round(change, 2))
        total_score += result
        total_opponent_rating += opp_rating

    # Итоговые значения
    total_change = sum(game_changes)
    avg_opponent_rating = round(total_opponent_rating / len(enemies))
    new_rating = round(hero_rating + total_change)
    performance_rating = round(avg_opponent_rating + 400 * (2 * total_score - len(enemies)) / len(enemies))


    return FCROutput(
        new_rating= max(int(new_rating), 1000),
        total_change=round(total_change, 2),
        game_changes= game_changes,
        performance=performance_rating,
        average_opponent_rating= avg_opponent_rating,
    )
