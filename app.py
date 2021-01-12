from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import *

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Note %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
@app.route('/home/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about/', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/new/', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        note_title = request.form['title']
        note_content = request.form['content']
        new_note = Note(title=note_title, content=note_content)

        try:
            db.session.add(new_note)
            db.session.commit()
            return redirect('/notes') 
        except:
            return 'There was an issue adding your note'

    else:
        #orderednotes = Note.query.order_by(Note.date_created).all()
        return render_template('new.html')

@app.route('/edit/', methods=['GET', 'POST'])
def edit_page():
    orderednotes = Note.query.order_by(Note.date_created.desc()).all()
    return render_template('edit.html', orderednotes=orderednotes)

@app.route('/delete/', methods=['GET', 'POST'])
def delete_page():
    orderednotes = Note.query.order_by(Note.date_created.desc()).all()
    return render_template('delete.html', orderednotes=orderednotes)

@app.route('/notes/', methods=['GET', 'POST'])
def notes():
    orderednotes = Note.query.order_by(Note.date_created.desc()).all()
    return render_template('notes.html', orderednotes=orderednotes)

@app.route('/delete/<int:id>/', methods=['GET', 'POST'])
def delete(id):
    note_to_delete = Note.query.get_or_404(id)

    try:
        db.session.delete(note_to_delete)
        db.session.commit()
        return redirect('/delete')
    except:
        return 'There was a problem deleting that note'

@app.route('/edit/<int:id>/', methods=['GET', 'POST'])
def edit(id):
    note = Note.query.get_or_404(id)

    if request.method == 'POST':
        note.content = request.form['content']
        note.title = request.form['title']

        try:
            db.session.commit()
            return redirect('/notes')
        except:
            return 'There was an issue updating your note'

    else:
        return render_template('editnote.html', note=note)


if __name__ == "__main__":
    app.run(debug=True)
