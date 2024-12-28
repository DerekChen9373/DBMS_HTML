from flask import Flask, render_template, request
app = Flask(__name__)

# 假設資料存儲結構
games = [
    {"id": 1, "name": "Game A", "year": 2020, "platform": "PC", "genre": "RPG", "global_sales": 1.5, "rating": 9.0},
    {"id": 2, "name": "Game B", "year": 2018, "platform": "PS4", "genre": "Action", "global_sales": 2.0, "rating": 8.5}
]

comments_data = {
    1: [{"comment_id": 101, "comment_text": "Great game!"}, {"comment_id": 102, "comment_text": "Loved it."}],
    2: [{"comment_id": 201, "comment_text": "Not bad."}, {"comment_id": 202, "comment_text": "Could be better."}]
}

@app.route("/comments/<int:game_id>")
def comments(game_id):
    game = next((g for g in games if g["id"] == game_id), None)
    comments = comments_data.get(game_id, [])
    return render_template("comments.html", game=game, comments=comments)
