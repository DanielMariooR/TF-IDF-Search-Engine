import os
import glob
from flask import Flask, render_template, flash, redirect, request,session
from werkzeug.utils import secure_filename
from search import cosine_similarity, HtmlParser, HtmlTitleParse, Preprocessing
from search import Querylib, Vectorizer,Sort, Wcounter, getFirstSen
from bs4 import BeautifulSoup



app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
app.config['SECRET_KEY'] = 'tubes algeo'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#Algoritma untuk melakukan multiple upload file
path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'static')

if not os.path.isdir(UPLOAD_FOLDER):
	os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt','html'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

#Route untuk mengakses halaman home/beranda
@app.route('/',methods=['GET','POST'])
def home():
	
	if(request.method=='POST'):
		query = form.request.get('search')
		if(query):
			redirect('/search_result')
	return render_template('index.html')

#Route untuk mengakses halaman perihal/about
@app.route('/about')
def about():
	return render_template('about.html')


#Route untuk melakukan upload multiple file
@app.route('/uploads', methods=['POST'])
def upload_file():
	if request.method == 'POST':

		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)

		files = request.files.getlist('files[]')

		for file in files:
			if file and allowed_file(file.filename):
				filename = file.filename
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

		flash('File(s) successfully uploaded')
		return redirect('/')

#Route untuk mengakses hasil pencarian
#
@app.route('/search_result', methods=['GET','POST'])
def search_result():

	results = []
	querylib = []
	query_term = 0
	qvector = []
	
	if(request.method=='POST'):

		query = request.form.get("search")

		if(query):
			#Proses Pre Processing (stemming dan stop words removal) serta vektorisasi query
			query_processed = Preprocessing(query)
			querylib = Querylib(query_processed)
			qvector = Vectorizer(querylib,query_processed)
			query_term = len(querylib)

			results = []
			filepath = './static/'
			for filename in glob.glob(os.path.join(filepath, '*.html')):
				with open(os.path.join(os.getcwd(),filename), 'r') as f:
					#Proses Pre Processing (stemming dan stop words removal) serta vektorisasi text dokumen
					#Hasil Preprocessing dan vektorisasi disimpan didalam tuple berisi (tingkat kemiripan, vektor,judul,kalimat pertama,link, jumlah kata)
					soup = BeautifulSoup(f, 'html.parser')
					text = HtmlParser(soup)
					title = HtmlTitleParse(soup)
					text_processed = Preprocessing(text)
					textlib = Querylib(text_processed)
					tqvector = Vectorizer(querylib,text_processed)
					tvector = Vectorizer(textlib,text_processed)
					sim = cosine_similarity(qvector,tqvector,tvector)
					numofwords = Wcounter(text)
					link = title + '.html'
					first_sentence = getFirstSen(text)
					res = (sim,tqvector,title,first_sentence,link,numofwords)
					results.append(res)

				Sort(results)  #Diurutkan berdasarkan tingkat kemiripan paling besar ke paling kecil
				len_result = len(results)
	return render_template('search_result.html', query=query, results=results, query_term=query_term, querylib=querylib,qvector=qvector,len_result=len_result)

