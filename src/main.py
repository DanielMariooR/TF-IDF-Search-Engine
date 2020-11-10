import os
from flask import Flask, render_template, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.config['SECRET_KEY'] = 'tubes algeo'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
	os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt','html'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello():
	return "Hello world!"

@app.route('/uploads')
def upload_form():
	return render_template('upload.html')

@app.route('/uploads', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/uploads')


class SearchBar(FlaskForm):
	search = StringField('Search', validators=[DataRequired()])

@app.route('/search', methods = ['GET', 'POST'])
def search():
	form = SearchBar()
	query = form.search.data
	return render_template('search.html', form=form, query=query)



