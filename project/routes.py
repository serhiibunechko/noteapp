from flask import render_template, redirect, url_for, request

from . import app, share
from .models import Message, db


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contacts')
def contacts():
    share.load()
    return render_template("contacts.html")


@app.route('/notes', methods=['GET'])
def notes():
    messages = Message.query.order_by(Message.date.desc()).all()
    return render_template("notes.html", messages=messages)


@app.route('/notes/<int:id>')
def notes_more(id):
     message = Message.query.get(id)
     return render_template('notes_more.html', message=message)


@app.route('/notes/<int:id>/delete')
def notes_delete(id):
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return redirect(url_for('notes'))


@app.route('/notes/<int:id>/update', methods=['GET', 'POST'])
def notes_update(id):
    message = Message.query.get(id)
    if request.method == 'POST':
        message.heading = request.form['heading']
        message.note = request.form['note']
        db.session.commit()
        return redirect(url_for('notes'))
    else:
        return render_template("update_notes.html", message=message)


@app.route('/create-note', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        heading = request.form['heading']
        note = request.form['note']
        new_note = Message(heading=heading, note=note)
        try:
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('notes'))
        except:
            return "Error"
    else:
        return render_template("create_note.html")
