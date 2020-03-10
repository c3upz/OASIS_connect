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

#defining the TWO routes the application needs

#'/' route leads to the homepage and runs when the application launches
@app.route('/')
def index():
    return render_template('index.html')

#'/result' route leads to the results page where we display the results from the search term
@app.route('/result')
def results():
    spreadsheetSelection = request.args.get("spreadsheetDropDown")
    #spreadsheetSelection = int(spreadsheetSelection)
    print(spreadsheetSelection)
    typeSearch = request.args.get("searchbox")
    print(typeSearch)  # this now prints out whatever was put in the searchbox
    dateSearch = 0
    dateSearch = request.args.get("dateDropDown")
    #this allows for the date search field to be left blank
    if dateSearch != '0': #if value is not '0' then make it an int bc the user has selected a date
        dateSearch = int(dateSearch)
    else: #otherwise the user selected '-' which cooresponds to value '0'.. here the user does not want to search by year
        dateSearch = ""
    #searchInput is an array of the search terms the user has inputed
    searchInput = [typeSearch,  dateSearch, '']
    myJSON = api.GET_REQUEST(spreadsheetSelection) #loads the spreadsheet data for given spreadsheet
    myOut = algos.search_function(myJSON, searchInput) #output after data was compared to search terms 
    #print(myOut)  # prints the array of ppl that it is returning
    return render_template('results.html', myJSON=myOut)


if __name__ == "__main__":
    app.run(debug=True)
