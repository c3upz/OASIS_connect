import json
import requests
from firebase import firebase

global URL 

URL = "https://oasis-initiative.firebaseio.com/15wNz3OyhjqzvmrATgRiaMFfK6IyZsLOx4sj0uBPVGO0/"
firebase = firebase.FirebaseApplication(URL)

"""
returns user's firstName, lastName, email, phone

    #PARAMS = users and their information from panel 'category'
    #RETURN = firstName, lastName, email, phone
"""
def get_basic_userInfo(category):
    result = firebase.get(category, '')
    return result

def get_specific_userInfo(id, category):
    result = get_basic_userInfo(category)
    return result[id]['firstName'], result[id]['lastName']
