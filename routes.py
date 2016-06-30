from flask import Flask, render_template
  
app = Flask(__name__)
  
@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/data')
def data():
  return render_template('data.html')
  
@app.route('/SHMI')
def SHMI():
  return render_template('SHMI.html')
  
@app.route('/observed')
def observed():
  return render_template('observed.html')
 
@app.route('/diagnosisgrouptable')
def diagnosisgrouptable():
  return render_template('diagnosisgrouptable.html')
  
@app.route('/thirtydays')
def thirtydays():
  return render_template('thirtydays.html')
   
@app.route('/expected')
def expected():
  return render_template('expected.html')

@app.route('/age')
def age():
  return render_template('age.html')
  
@app.route('/comorbidity')
def comorbidity():
  return render_template('comorbidity.html')
  
@app.route('/admission')
def admission():
  return render_template('admission.html')

@app.route('/gender')
def gender():
  return render_template('gender.html')
  
@app.route('/risk')
def risk():
  return render_template('risk.html')
  
if __name__ == '__main__':
  app.run(debug=True)