from flask import Flask, jsonify, request
from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import filtered_values
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "Success!"
    })

@app.route("/")
def articles():
    return jsonify({
        "data": all_articles,
        "status": "Success!"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    id = request.args.get("id")
    data = next(item for item in all_articles if item["id"] == id)
    all_articles.remove(data)
    liked_articles.append(data)
    return jsonify({
        "status": "Success!"
    }), 200

@app.route("/not-liked-article", methods=["POST"])
def not_liked_article():
    id = request.args.get("id")
    data = next(item for item in all_articles if item["id"] == id)
    all_articles.remove(data)
    not_liked_articles.append(data)
    return jsonify({
        "status": "Success!"
    }), 200

@app.route("/popular-articles")
def popular_articles():
    return jsonify({
        "data": filtered_values,
        "status": "Success!"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for article in liked_articles:
        output = get_recommendations(int(article['contentId']))
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "id": recommended[0],
            "index": recommended[1],
            "timestamp": recommended[2],
            "eventType": recommended[3],
            "contentId": recommended[4],
            "authorPersonId": recommended[5],
            "authorSessionId": recommended[6],
            "authorUserAgent": recommended[7],
            "authorRegion": recommended[8],
            "authorCountry": recommended[9],
            "contentType": recommended[10],
            "url": recommended[11],
            "title": recommended[12],
            "text": recommended[13],
            "lang": recommended[14],
            "total_events": recommended[15]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "Success!"
    }), 200

if __name__ == "__main__":
    app.run()