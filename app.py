from flask import Flask, request, jsonify

app = Flask(__name__)

serp_results = []

@app.route("/serp", methods=["POST"])
def create_search_result():
    data = request.get_json()
    if not data or not all(key in data for key in ["title", "url", "snippet"]):
        return jsonify({"error": "Missing required fields in request body"}), 400

    new_result = {
    "id": len(serp_results) + 1,  # Generate a simple ID for demonstration
    "title": data["title"],
    "url": data["url"],
    "snippet": data["snippet"],
}
    serp_results.append(new_result)
    return jsonify(new_result), 201

if __name__ == "__main__":
	app.run(debug=True)

