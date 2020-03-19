import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from form import QueryForm

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Migrate(app, db)

class Query(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)  # stulpelis, kurio reikšmės integer. Taip pat jis bus primary_key.
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.name, self.surname} - {self.message}"

@app.route("/", methods=['GET', 'POST'])
def index():
    db.create_all()
    form = QueryForm()
    if form.validate_on_submit():
        uzklausa = Query(name=form.name.data, surname=form.surname.data, email=form.email.data, phone=form.phone.data, message=form.message.data)
        db.session.add(uzklausa)
        db.session.commit()
        return query()
    return render_template("index.html", form=form)

@app.route("/query")
def query():
    try:
        data = Query.query.all()
    except:
        data = []
    return render_template("query.html", data=data)

@app.route("/delete/<int:id>")
def delete(id):
    uzklausa = Query.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return query()

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    form = QueryForm()
    uzklausa = Query.query.get(id)
    print("Redaguojama", uzklausa)
    # form.name.data = uzklausa.name
    # form.surname.data = uzklausa.surname
    # form.email.data = uzklausa.email
    # form.phone.data = uzklausa.phone
    # form.message.data = uzklausa.message
    if form.validate_on_submit():
        uzklausa.name = form.name.data
        uzklausa.surname = form.surname.data
        uzklausa.email = form.email.data
        uzklausa.phone = form.phone.data
        uzklausa.message = form.message.data
        db.session.commit()
        return query()
    return render_template("update.html", form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()
