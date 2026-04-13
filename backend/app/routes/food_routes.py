from flask import Blueprint, jsonify, request

from app.services.food_service import analyze_food_item

food_bp = Blueprint("food", __name__)


@food_bp.route("/", methods=["GET"])
def health_check():
    return "NutriCart API is running", 200


@food_bp.route("/analyze-food", methods=["POST"])
def analyze_food():
    payload = request.get_json(silent=True) or {}
    item = payload.get("item", "")

    if not isinstance(item, str) or not item.strip():
        return jsonify({"error": "'item' is required and must be a non-empty string."}), 400

    analysis = analyze_food_item(item)
    return jsonify(analysis), 200
