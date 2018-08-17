from flask import Flask, render_template 

application = app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/siteinfo')
def siteinfo():
	return render_template('siteinfo.html')


if __name__ == "__main__":
	app.run(debug=True)
