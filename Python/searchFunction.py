spreadsheet_data = [{'firstName': 'Cris',
'city': 'Lagos', 
'gender': 'male', 
'id': 1, 
'lastName': 'Gerb', 
'nom_indiv': 'nominee', 
'occupation': 'Software Engineer',
'slp_domain': 'Scars', 
'slp_year': 2016}, 

{'firstName': 'Haye', 
'city': 'Cairo',
'gender': 'male', 
'id': 2, 
'lastName': 'Fits', 
'nom_indiv': 'nominee', 
'slp_domain': 'GoDaddy',
'occupation': 'Mechanical Engineer',
'slp_year': 1995}]

searchInput = ['Lagos', 'Software Engineer', 2016]

def search_function(spreadsheet_data, searchInput):
    myOut = []  # output array for matches
    checker = len(searchInput)  #  checks to make sure # of inputs is equal to # of matches
    dynamic_checks = 0  # incrementer for checking INDEX-OUT-OF-BOUNDS
    matches = 0 # counts number of matches 

    # first, loop through array of json objects
    for i in spreadsheet_data:
        # second, loop through key:value pairs per json
        for j, k in i.items():
            if (dynamic_checks <= checker-1):   # check to make sure no index out of bounds
                # if searchInput field == value in JSON, it's a match
                if (searchInput[dynamic_checks] == k): 
                    matches += 1
                    dynamic_checks += 1
        # if number of matches == # of inputs given, add to output array
        if (matches == checker):
            myOut.append(i)
            matches = 0 # reset incremementer for next JSON object
    return myOut

myOut = search_function(spreadsheet_data, searchInput)
print (myOut)

    

