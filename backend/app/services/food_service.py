from app.utils.formatters import normalize_food_item

FOOD_DATASET = {
    "banana": {"calories": 105, "protein": 1.3, "sugar": 14.4, "fiber": 3.1},
    "apple": {"calories": 95, "protein": 0.5, "sugar": 19.0, "fiber": 4.4},
    "burger": {"calories": 354, "protein": 17.0, "sugar": 5.0, "fiber": 1.2},
    "soda": {"calories": 150, "protein": 0.0, "sugar": 39.0, "fiber": 0.0},
    "rice": {"calories": 206, "protein": 4.3, "sugar": 0.1, "fiber": 0.6},
    "chicken": {"calories": 165, "protein": 31.0, "sugar": 0.0, "fiber": 0.0},
    "oats": {"calories": 307, "protein": 10.7, "sugar": 1.1, "fiber": 8.1},
    "broccoli": {"calories": 55, "protein": 3.7, "sugar": 1.5, "fiber": 5.1},
    "egg": {"calories": 78, "protein": 6.3, "sugar": 0.6, "fiber": 0.0},
    "salmon": {"calories": 233, "protein": 25.0, "sugar": 0.0, "fiber": 0.0},
}


def _calculate_health_score(nutrition: dict) -> int:
    score = 70

    sugar = nutrition["sugar"]
    fiber = nutrition["fiber"]
    protein = nutrition["protein"]
    calories = nutrition["calories"]

    # High sugar reduces score.
    if sugar > 30:
        score -= 25
    elif sugar > 20:
        score -= 15
    elif sugar > 10:
        score -= 8

    # High fiber increases score.
    if fiber >= 8:
        score += 16
    elif fiber >= 5:
        score += 10
    elif fiber >= 3:
        score += 6

    # Balanced macros increase score.
    protein_density = protein / max(calories, 1) * 100
    sugar_density = sugar / max(calories, 1) * 100

    if protein_density >= 5 and sugar_density <= 8:
        score += 12
    elif protein_density >= 3 and sugar_density <= 10:
        score += 7

    return max(0, min(100, round(score)))


def _build_explanation(item: str, nutrition: dict, matched_dataset: bool) -> str:
    source = "known nutrition data" if matched_dataset else "estimated values"
    return (
        f"{item} was analyzed using {source}. "
        f"Sugar ({nutrition['sugar']}g) and fiber ({nutrition['fiber']}g) were weighted, "
        "and macro balance was considered in the score."
    )


def analyze_food_item(item: str) -> dict:
    normalized_item = normalize_food_item(item)

    nutrition = FOOD_DATASET.get(normalized_item)
    matched_dataset = nutrition is not None

    if nutrition is None:
        nutrition = {"calories": 180, "protein": 6.0, "sugar": 9.0, "fiber": 2.0}

    health_score = _calculate_health_score(nutrition)

    return {
        "item": normalized_item,
        "health_score": health_score,
        "calories": nutrition["calories"],
        "protein": nutrition["protein"],
        "sugar": nutrition["sugar"],
        "fiber": nutrition["fiber"],
        "confidence": "high" if matched_dataset else "low",
        "short_explanation": _build_explanation(normalized_item, nutrition, matched_dataset),
    }
