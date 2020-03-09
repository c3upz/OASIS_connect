# flask and firebase
from firebase import firebase
from flask import Flask, render_template, request, redirect
import requests
import json
import sys

sys.path.insert(1, 'modules/')  # append modules path
# import classes
import userInfo
import api
import algos

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Flask tests
@app.route('/result')
def results():
    spreadsheetSelection = request.args.get("spreadsheetDropDown")
    #spreadsheetSelection = int(spreadsheetSelection)
    print(spreadsheetSelection)
    typeSearch = request.args.get("searchbox")
    print(typeSearch) #this now prints out whatever was put in the searchbox
    dateSearch = 0
    dateSearch = request.args.get("dateDropDown")
    if dateSearch != '0':
        dateSearch = int(dateSearch)
    else:
        dateSearch = ""
    print(dateSearch)
    searchInput = [typeSearch,  dateSearch, '']
    print (searchInput)
    # myJSON = api.GET_REQUEST('Mentor')
    myJSON = api.GET_REQUEST(spreadsheetSelection)
    myOut = algos.search_function(myJSON, searchInput)
    print(myOut) #prints the array of ppl that it is returning
    return render_template('results.html', myJSON = myOut)


# @app.route("/modulesTest")
# def modulesTest():
#   firstName,lastName = userInfo.get_specific_userInfo(1, 'Mentor')
#   return render_template('modulesTest.html', firstName=firstName, lastName=lastName)

# @app.route('/forms', methods=['POST'])
# def my_form_data():
#   text = request.form['text']
#   processed_text = text.upper()
#   return processed_text

# @app.route("/html_req_test")
# def getEmail():
#   email = html_req_test()
#   return render_template('html_req_test.html', email=email)


if __name__ == "__main__":
    app.run(debug=True)
