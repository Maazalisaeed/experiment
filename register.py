@app.route("/register", methods=["GET", "POST"])
def register():

    # check if the request method is post(ie submiting form)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT username FROM users WHERE username = :username",username = request.form.get("username"))

        if len(rows) != 1:
            return apology("Username Already exist")
        db.execute("INSERT INTO users (username, hash) VALUES(? , ?)", username = request.form.get("username"), password = request.form.get("password"))
        return redirect("/login")
    else:
        return render_template("register.html")
