# -*- coding: utf-8 -*-

import time
from flask import Flask, flash, render_template, session, redirect, url_for, request
import hashlib

from data import VALID_VALGFAG, data, DEFAULT_SESSION, VALID_STUDY_FIELDS
from structures import User

app = Flask(__name__)
app.secret_key = b'_5#y2L"2\n\xec]/'


def repr(value: object):
    return value.__repr__()


app.jinja_env.filters["repr"] = repr

all_reviews = data["reviews_for_studieretninger"] + data["reviews_for_valgfag"]
last_endpoint = "home"


@app.before_request
def pre_request():
    if not "session" in session:
        session["session"] = DEFAULT_SESSION


@app.context_processor
def app_context():
    return session["session"]


@app.route("/")
def home():
    last_endpoint = "home"
    # the reviews on the homepage will always be filtered by the newest ones.
    all_reviews.sort(key=lambda x: x["posted"], reverse=True)

    return render_template(
        "homepage.html",
        reviews=all_reviews,
    )


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        pwhash = hashlib.md5(request.form["password"].encode())
        username = request.form["username"].lower().replace(" ", "_")
        display = request.form["display"]
        field_of_study = int(request.form["field_of_study"])
        optional_subject = int(request.form["subject"])
        grade = request.form["grade"].upper()

        u = User(
            password=pwhash.hexdigest(),
            username=username,
            display=display,
            id=len(data["users"]),
            grade=grade,
            field_of_study=VALID_STUDY_FIELDS[field_of_study],
            optional_subject=VALID_VALGFAG[optional_subject],
        )

        data["users"].append(u)
        session["session"] = u.__dict__ | {"logged_in": True}
        return redirect(url_for("home"))

    return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        hash = hashlib.md5(request.form["password"].encode())
        uname = request.form["username"]

        for u in data["users"]:
            if u.username == uname:
                user = u
                break
        else:
            error = "Dit brugernavn og kodeord passer ikke."
            return render_template("login.html", error=error)

        if user.get_password() != hash.hexdigest():
            error = "Dit brugernavn og kodeord passer ikke."
            return render_template("login.html", error=error)

        session["session"] = u.__dict__ | {"logged_in": True}
        return redirect(url_for("home"))

    return render_template("login.html")


@app.post("/logout")
def logout():
    session["session"] = DEFAULT_SESSION

    return redirect(url_for("home"))


@app.get("/studieretninger")
def review_listing():
    last_endpoint = "review_listing"

    return render_template(
        "studieretninger.html", reviews=data["reviews_for_studieretninger"]
    )


@app.get("/valgfag")
def review_valgfag_listing():
    last_endpoint = "review_valgfag_listing"
    return render_template("valgfag.html", reviews=data["reviews_for_valgfag"])


@app.get("/review/<id>")
def review(id: int):
    last_endpoint = "review"
    r = None
    for review in all_reviews:
        if review["id"] == int(id):
            r = review
            break
    else:
        return redirect(url_for("home"))

    return render_template("review.html", review=r)


@app.post("/delete/<id>")
def delete_review(id: int):
    if not session["session"]["logged_in"]:
        return redirect(url_for("reviews"))

    r = None
    for review in all_reviews:
        if review["id"] == int(id) and review["user"]["id"] == session["session"]["id"]:
            r = review
            break
    else:
        return redirect(url_for("reviews"))

    all_reviews.remove(r)

    if r in (s := data["reviews_for_studieretninger"]):
        s.remove(r)
    elif r in (v := data["reviews_for_valgfag"]):
        v.remove(r)

    return redirect(url_for("reviews"))


@app.route("/edit/<id>", methods=["POST", "GET"])
def edit_review(id):
    if request.method == "POST":
        return redirect(url_for("reviews"))
    last_endpoint = "edit_review"

    if not session["session"]["logged_in"]:
        return redirect(url_for("reviews"))

    r = None
    for review in all_reviews:
        if review["id"] == int(id):
            r = review
            break
    else:
        return redirect(url_for("reviews"))

    return render_template("review.html", review=r)


@app.get("/reviews")
def reviews():
    last_endpoint = "reviews"
    if not session["session"]["logged_in"]:
        return redirect(url_for("login"))

    r = []

    for review in all_reviews:
        if review["user"]["id"] == session["session"]["id"]:
            r.append(review)

    return render_template("reviews.html", reviews=r)


@app.route("/opret", methods=["POST", "GET"])
def create_review():
    if not session["session"]["logged_in"]:
        exit(1)

    if request.method == "POST":
        category = int(request.form["category"])
        path = ["reviews_for_studieretninger", VALID_STUDY_FIELDS]

        if category > len(VALID_STUDY_FIELDS):
            path = ["reviews_for_valgfag", VALID_VALGFAG]
            category -= len(VALID_STUDY_FIELDS)
        elif category > len(VALID_VALGFAG):
            print("category doesn't exist")
            return render_template("oprettelse.html")
        print(category)
        print(path[0])
        input = {
            "posted": int(time.time()),
            "user": session["session"],
            "id": (new_id := len(all_reviews) + 1),
            "title": request.form["title"],
            "content": request.form["content"],
            "hearts": 0,
            "rating": float(request.form["rating"]),
            "comments": [],
        }

        if path[0] == "reviews_for_studieretninger":
            input |= {"field_of_study": path[1][category]}
        else:
            input |= {"subject": path[1][category]}

        data[path[0]].append(input)
        all_reviews.append(input)
        all_reviews.sort(key=lambda x: x["posted"], reverse=True)
        data[path[0]].sort(key=lambda x: x["posted"], reverse=True)

        return redirect(url_for("review", id=new_id))
    last_endpoint = "opret"
    return render_template("oprettelse.html")


@app.post("/create_comment/<review_id>")
def create_comment(review_id: int):
    if not session["session"]["logged_in"]:
        exit(1)

    pos = 0
    for review in all_reviews:
        if review["id"] == int(review_id):
            break
        pos += 1

    if len(all_reviews) - 1 < pos:
        print("whoopsies")
        return redirect(url_for("review", id=review_id))

    input = {
        "user": session["session"],
        "content": request.form["content"],
        "hearts": 0,
    }

    all_reviews[pos]["comments"].append(input)
    return redirect(url_for("review", id=review_id))


@app.post("/like/<id>")
def like_review(id: int):
    for r in all_reviews:
        if r["id"] == int(id):
            r["hearts"] += 1

    for r in data["reviews_for_studieretninger"]:
        if r["id"] == int(id):
            r["hearts"] += 1

    for r in data["reviews_for_valgfag"]:
        if r["id"] == int(id):
            r["hearts"] += 1

    # {session.id: [review_id]}

    # if this is true, it's a unheart or unlike.
    # if (
    #     session["session"]["id"] in data["likes"]
    #     and id in data["likes"][session["session"]["id"]]
    # ):
    #     data["likes"][session["session"]["id"]].pop(int(id))
    #     all_reviews[pos]["hearts"] -= 1
    # else:
    #     try:
    #         data["likes"][session["session"]["id"]].append(int(id))
    #     except:
    #         data["likes"][session["session"]["id"]] = [int(id)]

    return redirect(url_for(last_endpoint, id=id))


if __name__ == "__main__":
    app.run(debug=True)
