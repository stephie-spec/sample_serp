from flask import Flask, request, jsonify
from app import db, models

app = Flask(__name__)

@app.route("/serp", methods=["POST"])
def create_search_result():
  data = request.get_json()
  if not data or not all(key in data for key in ["title", "url", "snippet"]):
    return jsonify({"error": "Missing required fields in request body"}), 400

  new_result = models.SearchResult(title=data["title"], url=data["url"], snippet=data["snippet"])
  db.session.add(new_result)
  db.session.commit()

  return jsonify(new_result.serialize()), 201  # Return serialized data

# Define helper method for serialization (optional)
def serialize(obj):
  return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

