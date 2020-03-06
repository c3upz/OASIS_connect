import requests
import json
import sys
sys.path.insert(1, 'modules/')  # append modules path
# import classes
import userInfo
import api
import algos
# flask and firebase
from firebase import firebase 
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>This is the homepage</h1>"

# Flask tests
@app.route("/prototype")
def prototype():
  searchInput = ['Boureima',  'GADO', 'boureima_gado@yahoo.fr']

  myJSON = api.GET_REQUEST('Mentor')
  myOut = algos.search_function(myJSON, searchInput)
  return render_template('prototype.html', myJSON= myOut)

@app.route("/modulesTest")
def modulesTest():
  firstName,lastName = userInfo.get_specific_userInfo(1, 'Mentor')
  return render_template('modulesTest.html', firstName=firstName, lastName=lastName)

@app.route('/forms', methods=['POST'])
def my_form_data():
  text = request.form['text']
  processed_text = text.upper()
  return processed_text

# @app.route("/html_req_test")
# def getEmail():
#   email = html_req_test()
#   return render_template('html_req_test.html', email=email)


if __name__ == "__main__":
  app.run(debug=True)

