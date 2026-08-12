from datetime import date

from flask import Flask, flash, redirect, render_template, request, url_for

from config import Config
from models import Application, db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/applications")
def applications():
    applications = db.session.execute(db.select(Application)).scalars().all()
    return render_template("applications.html", applications = applications)


@app.route("/applications/<int:id>/delete", methods=["POST"])
def delete_application(id):
    application = db.get_or_404(Application, id)
    db.session.delete(application)
    db.session.commit()
    flash('Deleted', "success")
    return redirect(url_for("applications"))


@app.route("/applications/<int:id>/edit", methods=["GET", "POST"])
def edit_application(id):
    application = db.get_or_404(Application, id)
    if request.method == "POST":
        deadline_raw = request.form.get("deadline")
        deadline = date.fromisoformat(deadline_raw) if deadline_raw else None

        application.company = request.form.get("company")
        application.role = request.form.get("role")
        application.location = request.form.get("location")
        application.job_url = request.form.get("job_url")
        application.deadline = deadline
        application.status = request.form.get("status")
        application.job_desc = request.form.get("job_desc")
        application.notes = request.form.get("notes")
        db.session.commit()
        flash('Edited', "success")
        return redirect(url_for('applications'))
    return render_template("edit_application.html", application = application)


@app.route("/add-application", methods=["GET", "POST"])
def add_application():
    if request.method == "POST":
        deadline_raw = request.form.get("deadline")
        deadline = date.fromisoformat(deadline_raw) if deadline_raw else None
        
        application = Application(
            company = request.form.get("company"),
            role = request.form.get("role"),
            location = request.form.get("location"),
            job_url = request.form.get("job_url"),
            deadline = deadline,
            status = request.form.get("status"),
            job_desc = request.form.get("job_desc"),
            notes = request.form.get("notes")
        )
        db.session.add(application)
        db.session.commit()
        flash('Saved', "success")
        return redirect(url_for('applications'))
    return render_template("add_application.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)