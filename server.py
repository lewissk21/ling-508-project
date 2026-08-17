from flask import Flask, jsonify
from flask_cors import CORS
from app.services import Services

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

services = Services()


def _serialize(restaurant) -> dict:
    return {
        "name": restaurant.name,
        "address": restaurant.address,
        "website": restaurant.website,
    }


@app.route('/')
def doc():
    app.logger.info("doc - Got request")
    return jsonify({
        "endpoints": [
            "GET /get-all-restaurants",
            "GET /find-restaurants-by-dish/<dish_name>",
        ]
    })

# route for finding restaurants by dish
@app.route('/find-restaurants-by-dish/<dish_name>', methods=['GET'])
def find_restaurants_by_dish(dish_name: str):
    app.logger.info(f"find-restaurants-by-dish - Got request: {dish_name}")
    restaurants = services.find_restaurants_by_dish(dish_name)
    app.logger.info(f"find-restaurants-by-dish - Output: {restaurants}")
    return jsonify([_serialize(r) for r in restaurants])

# route for getting all restaurants
@app.route('/get-all-restaurants', methods=['GET'])
def get_all_restaurants():
    app.logger.info("get-all-restaurants - Got request")
    restaurants = services.get_all_restaurants()
    app.logger.info(f"get-all-restaurants - Output: {restaurants}")
    return jsonify([_serialize(r) for r in restaurants])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
