from app.utils.formatters import normalize_food_item


def analyze_food_item(item: str) -> dict:
    normalized_item = normalize_food_item(item)

    return {
        "item": normalized_item,
        "health_score": 86,
        "calories": 105,
        "short_explanation": f"{normalized_item} is generally nutrient-dense and a healthy everyday choice.",
    }
