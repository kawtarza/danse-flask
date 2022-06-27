from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template ('home.html')
  

  
@app.route('/nosprix')
def nosprix():
  return render_template ('nosprix.html')

@app.route('/notreequipe')
def notreequipe():
  return render_template ('notreequipe.html')
  
@app.route('/contact')
def contact():
  skip = True
  return render_template('contact.html', skip_fixed_top= skip)

app.run(host='0.0.0.0', port=81)