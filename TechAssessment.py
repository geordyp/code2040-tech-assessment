# my API token: 30e2d792d1001d661697aed566e0341a

import json
import urllib2

# create_HTTP_request() creates an http request and returns the response
# http://www.stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json
#
# @param {String} targetURL
# @param {JSON} dictionary
# @return {Object} response - file like object
def create_HTTP_request(targetURL, dictionary):
    request = urllib2.Request(targetURL)
    request.add_header('Content-Type', 'application/json')
    return urllib2.urlopen(request, json.dumps(dictionary))

# this endpoint will return a JSON with keys 'prefix' and 'array'
targetURL = 'http://challenge.code2040.org/api/prefix'
dictionary = {'token': '30e2d792d1001d661697aed566e0341a'}
response = create_HTTP_request(targetURL, dictionary)

# {'prefix': ---, 'array': [---, ---, ---, ...]}
input = json.load(response)
prefix = input['prefix']

# find the words in the array that DON'T start with the given prefix
output = []
prefixLength = len(prefix)
arraySize = len(input['array'])
for i in range(0, arraySize):
    currentWord = input['array'][i]
    if currentWord[0:prefixLength] != prefix:
        # found a word that DOESN'T start with the prefix
        output.append(currentWord)

# return the list of words that DON'T start with the given prefix
targetURL = 'http://challenge.code2040.org/api/prefix/validate'
dictionary = {'token': '30e2d792d1001d661697aed566e0341a', 'array': output}
create_HTTP_request(targetURL, dictionary)
