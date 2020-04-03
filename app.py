from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_pokemon

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost/pokedex"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost/pokedex")


@app.route("/")
def index():
    listings = mongo.db.pokemon.find_one()
    return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():
    listings = mongo.db.name
    listings_data = scrape_pokemon.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

