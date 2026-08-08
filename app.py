from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # Change this so its not public knowledge

applications_stored = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/applications")
def applications():
    return render_template("applications.html", applications = applications_stored)


@app.route("/add-application", methods=["GET", "POST"])
def add_application():
    if request.method == "POST":
        applications_stored.append({
            "company": request.form.get("company"),
            "role": request.form.get("role"),
            "location": request.form.get("location"),
            "jobURL": request.form.get("jobURL"),
            "deadline": request.form.get("deadline"),
            "status": request.form.get("status"),
            "jobDesc": request.form.get("jobDesc"),
            "notes": request.form.get("notes")
        })
        flash('Saved', "success")
        #print(applications_stored)
        return redirect(url_for('applications'))
    return render_template("add_application.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)