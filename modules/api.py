import requests
import json
from firebase import firebase 


# global variables
global API_ENDPOINT
global API_KEY
global URL
global STORAGE_URL

API_ENDPOINT = ""
API_KEY = ""
URL = "https://oasis-initiative.firebaseio.com/15wNz3OyhjqzvmrATgRiaMFfK6IyZsLOx4sj0uBPVGO0/"
STORAGE_URL = ""

firebase = firebase.FirebaseApplication(URL)

"""======================================================================"""
""" Send JSON to Data File (GET file)

    # PARAMS = result
    # DESC   = method to send GET data to file
"""
def GET_sendJSON_to_outfile(result):
  try:
    myJson = json.dumps(result, indent=4)
    #print("JSON GET Method", myJson, "\n===================================")

    with open('test.txt', 'w') as outfile: #wtf is this doing lol
        json.dump(data, outfile)

  except json.JSONDecodeError as err:
    print ("An error occurred: {}".format(err))

"""======================================================================"""
""" API POST REQUEST Method:

  # PARAMS = 'category'   'data' 
  # DESC   = Choose which tab of the Firebase-Sheets RLTDB is desired
  #          Data to POST          
"""
def POST_REQUEST(category, data):

  result = firebase.post(category, data)
  print ("Posting Method", result, "\n===================================")

# temporarily created POST data
data = {
  'ID': 22,
  'Name': 'testuser',
  'Email': 'testuser@g.com',
  'Phone': 123-456-7890
}
# USAGE: POST_REQUEST('Prototype', data)

"""======================================================================"""
""" API GET REQUEST Method:

  # PARAMS = 'category'
  # DESC   = Choose which tab of the Firebase-Sheets RTDB is desired
  # RETURN = Returns the parsed JSON file 
"""
def GET_REQUEST(category):

  result = firebase.get(category, '') 
  # print ("Entire result:", result) # print all data for debug

  # send data to the output file
  GET_sendJSON_to_outfile(result)
  return result[1:]