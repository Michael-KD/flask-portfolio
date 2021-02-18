from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import *
import re
import random
from pytube import YouTube
from PyDictionary import PyDictionary
dictionary=PyDictionary()

import ctypes  # An included library with Python install.   

wordList = ['abate', 'aberration', 'abhor', 'abhorrence', 'abstruse', 'accost', 'acrimony', 'acumen', 'adamant', 'adept', 'adroit', 'affected', 'alacrity', 'allocate', 'altruistic, altruism', 
'amenable', 'amiable', 'amicable', 'antediluvian', 'anthropology', 'antipathy', 'apathetic, apathy', 'apt', 'arcane', 'ascendancy', 'ascetic, asceticism', 'aspire', 'assail', 'assiduous', 'assuage', 'atrophy', 'attenuate', 'august', 'aura', 'auspicious', 'autocrat, autocratic', 'automaton', 'avarice', 'banal', 'barrage', 'belie', 'belligerent', 'benevolent', 'bequeath', 'berate', 'bipartisanship', 'blighted', 'bog', 'bolster', 'bombastic', 'boorish', 'boorishness', 'buoyant', 'burgeon', 'buttress', 'byzantine', 'cacophonous', 'cacophony', 'cajole', 'callous', 'cantankerous', 'capricious', 'castigate', 'caustic', 'censorious', 'censure', 'cerebral', 'chagrin', 'charlatan', 'chastise', 'chide', 'churlish', 
'circuitous', 'circumscribe', 'circumvent', 'clandestine', 'coalesce', 'compendious', 'complacency, complacent', 'compliant', 'compliance', 'conciliate', 'conciliatory', 'concur', 'conflagration', 'confluence', 'congenial', 'conscientious', 'consternation', 'contempt', 'contemptible', 'contentious', 'convivial', 'copious', 'corroborate', 'cosmopolitan', 
'credulity', 'credulous', 'culpable', 'cursory', 'dauntless', 'dearth', 'debacle', 'debilitate', 'debunk', 'decimate', 'decorum', 'decorous', 'deference', 'deferential', 'degradation', 'deleterious', 'delineate', 'demonstrative', 'demure', 'demurral', 'demystify', 'denigrate', 'depose', 'depravity', 'deprecate', 'depreciation', 'depreciatory', 'deride', 'derivative', 'derogatory', 'derogate', 'desecration', 'despondent', 'despot', 'destitute', 'deterrent', 'devoid', 'didactic', 'diffident', 'diffidence', 'diffuse', 'digress', 'digression', 'dilatory', 'diminutive', 'diminution', 'dire', 'discern', 'discomfited', 'disheartening', 'disillusionment', 'disingenuous', 'disparage', 'dispassionate', 'dispel', 'disputatious', 'disquiet', 'disquieting', 'disseminate', 'distaste', 'divergent', 'divisive', 'divulge', 'doctrine', 'dogmatic', 'dormant', 'dupe', 'duplicitous', 'duplicity', 'ebullient', 'eclectic', 'efface', 'effacement', 'effervesce', 'egalitarian', 'elated', 'elicit', 'elucidate', 'elude', 'elusive', 'embitter', 'embroil', 'empathetic, empathy', 'empiric', 'empirical', 'encompass', 'encroaching', 'encumbrance', 'enigmatic', 'enumerate', 'ephemeral', 'epiphany', 'epitome', 'equanimity', 'equitable', 'equivocal', 'erudite', 'erudition', 'esoteric', 'estrange', 'eulogy', 'eulogize', 'evoke', 'exacting', 'excavate', 'exemplar', 'exhibitionist', 'exhort', 'exorbitant', 'expedient', 'extol', 'extricate', 'facile', 'faction', 'fallacious', 'fallacy', 'fanaticism', 'fastidious', 'fathom', 'felicitous', 'finesse', 'flagrant', 'flippant', 'flippancy', 'florid', 'floridity', 'flummox', 'folly', 'foolhardy', 'forlorn', 'fortitude', 'fortuitous', 'fraudulent', 'frugality', 'furor', 'furtive', 'futile', 'futility', 'gait', 'gallant', 'gallantry', 'gargantuan', 'garish', 'genial', 'germinate', 'glutton', 'grandiose', 'hackneyed', 'hamper', 'hardy', 'hasten', 'heresy', 'heretic', 'histrionic', 'hubris', 'idiosyncrasy', 'idiosyncratic', 'idyllic', 'ignominy', 'ignominious', 'illicit', 'impasse', 'imperious', 'impetuous', 'impudence', 'impudent', 'inane', 'incongruity', 'incongruous', 'incredulous', 'incredulity', 'incriminate', 'incubate', 'indeterminate', 'indict', 'indictment', 'indigenous', 'indignant', 'indiscriminate', 'indolent', 'indomitable', 'induce', 'indulgent', 'ineffable', 'ineptitude', 'inert', 'inertia', 'ingenuous', 'inherent', 'inhibit', 'innate', 'innocuous', 'innuendo', 'inscrutable', 'insipid', 'insolence, insolent', 'instigate', 'insular', 'insularity', 'intrepid', 'inundate', 'invoke', 'irate', 'irony, ironic', 'irreverent', 'irreverence', 'jaded', 'jocular', 'jovial', 'judicious', 'lackadaisical', 'laconic', 'laggard', 'languid', 'latent, latency', 'laud', 'laudatory', 'listless', 'lithe', 'lucid', 'lucrative', 'lull', 'lurid', 'luxuriant', 'magnanimity', 'magnanimous', 'malleable', 'marred', 'maudlin', 'melancholy', 'mercenary', 'mercurial', 'miserly', 'mitigate', 'mitigator', 'modicum', 'morose', 'motley', 'multifarious', 'nebulous', 'nefarious', 'neophyte', 'notoriety', 'notorious', 'noxious', 'nuance', 'obdurate', 'obstinate', 'obstinacy', 'officious', 'onerous', 'opportunist', 'opportunistic', 'oracle', 'orthodox', 'ostensible', 'oversight', 'pacifist', 'pacify', 'painstaking', 'palliate', 'palliative', 'paradigm', 'parch', 'parody', 'partisan', 'patronize', 'paucity', 'pedant', 'pedantic', 'pedantry', 'peevish', 'penchant', 'penurious', 'peremptory', 'perfunctory', 'peripheral', 'perquisite', 'petulant', 'philanthropist', 'philanthropic', 'piety', 'pious', 'placate', 'placid', 'plasticity', 'plausible', 'plausibility', 'plethora', 'plethoric', 'pliable', 'pliant', 'polemical', 'prattle', 'precarious', 'precipitate', 'preclude', 'precocious', 'presumptuous', 'pretext', 'prevaricator', 'procure', 'prodigious', 'profound', 'profundity', 'profuse', 'profusion', 'prohibitive', 'prohibition', 'proliferate', 'proliferation', 'prolific', 'pronouncement', 'propensity', 'proponent', 'prosaic', 'prospective', 'provident', 'provincial', 'punctilious', 'pundit', 'quell', 'quixotic', 'rampant', 'ramshackle', 'rancor', 'rancorous', 'rapport', 'ratify', 'raucous', 'ravenous', 'raze', 'reap', 'rebuttal', 'recalcitrant', 'recant', 'recessive', 'recluse', 'reclusive', 'rectify', 'rectitude', 'redolent', 'refutation', 'refute', 'regressive', 'relegate', 'relinquish', 'renounce', 'repertory', 'reprehensible', 'reprimand', 'reproach', 'repudiate', 'repugnant', 'rescind', 'reticent, reticence', 'reverent', 'rhetoric', 'rhetorician', 'rouse', 'rousing', 'sage', 'sanctimonious', 'sanction', 'sanctity', 'sanguine', 'satiate', 'satire', 'satirical', 'satirize', 'saturate', 'scanty', 'scathing', 'scintillating', 'scope', 'scrupulous', 'scrutinize', 'scrutiny', 'self-righteous', 'self-serving', 'serendipity', 'servile', 'shrewd', 'shroud', 'simile', 'slight', 'slipshod', 'solace', 'solicitous', 'solicitousness', 'somber', 'sophistry', 'spartan', 'sporadic', 'spurious', 'spurn', 'squander', 'stagnant', 'stagnation', 'stark', 'starkness', 'static', 'staunch', 'steadfast', 'stock', 'strident', 'stupefy', 'stupefaction', 'subservient', 'substantiate', 'subversive', 'succulent', 'supercilious', 'superfluous', 'supplant', 'surfeit', 'susceptible', 'sycophant', 'tangential', 'teem', 'teeming', 'temperamental', 'temporize', 'tenacious, tenacity', 'tenuous', 'tirade', 'toady', 'torpor', 'totalitarian', 'tout', 'tractable', 'transient', 'treatise', 'trepidation', 'tribulation', 'trifling', 'trite', 'truculent, truculence', 'ubiquitous', 'unabashed', 'uncanny', 'uncouth', 'unfathomable', 'ungainly', 'unruly', 'unwitting', 'urbane', 'usurp', 'vacuous', 'vacuity', 'vanquish', 'vapid', 'venal', 'venality', 'venerable', 'verbose', 'vicarious', 'vigilant', 'vindicate', 'vindication', 'vindictive', 'virtuoso', 'virtuosity', 'virulent', 'viscous', 'vocation', 'vying', 'waning', 'wayward', 'wrath', 'wry', 'zealot']

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

@app.route('/animations/', methods=['GET', 'POST'])
def animations():
    return render_template('animations.html')

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



@app.route('/wordgames/', methods=['GET', 'POST'])
def wordgames():
    if request.method == 'POST':
        word = random.choice(wordList)
        wordDef = dictionary.meaning(word)
        wordDef = str(wordDef)
        wordDef = wordDef[1:-1]
        return render_template('wordgames.html', word = word, wordDef = wordDef)
    
    else:
        word = random.choice(wordList)
        wordDef = dictionary.meaning(word)
        wordDef = str(wordDef)
        wordDef = wordDef[1:-1]
        return render_template('wordgames.html', word = word, wordDef = wordDef)

@app.route('/wordscramble/', methods=['GET', 'POST'])
def wordscramble():
    if request.method == 'POST':
        word = random.choice(wordList)
        wordDef = dictionary.meaning(word)
        wordDef = str(wordDef)
        wordDef = wordDef[1:-1]
        return render_template('wordscramble.html', word = word, wordDef = wordDef)
    
    else:
        word = random.choice(wordList)
        wordDef = dictionary.meaning(word)
        wordDef = str(wordDef)
        wordDef = wordDef[1:-1]
        return render_template('wordscramble.html', word = word, wordDef = wordDef)

@app.route('/hangman/', methods=['GET', 'POST'])
def hangman():
    if request.method == 'POST':
        word = random.choice(wordList)
        wordDef = dictionary.meaning(word)
        wordDef = str(wordDef)
        wordDef = wordDef[1:-1]
        return render_template('hangman.html', word = word, wordDef = wordDef)
    
    else:
        word = random.choice(wordList)
        wordDef = dictionary.meaning(word)
        wordDef = str(wordDef)
        wordDef = wordDef[1:-1]
        return render_template('hangman.html', word = word, wordDef = wordDef)

@app.route('/youtube', methods=['GET', 'POST'])
def youtube():
    if request.method == 'POST':
        #try:
            link = request.form['link']
            yt = YouTube(link)
            ys = yt.streams.get_highest_resolution()
            ys.download()
            return render_template('youtube.html')
        #except:
            return render_template('youtube.html')

    else:
        return render_template('youtube.html')


if __name__ == "__main__":
    app.run(debug=True)
