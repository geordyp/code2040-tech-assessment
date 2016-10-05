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

# this endpoint will return a string and an array containing that string along with others
targetURL = 'http://challenge.code2040.org/api/haystack'
dictionary = {'token': '30e2d792d1001d661697aed566e0341a'}
response = create_HTTP_request(targetURL, dictionary)

input = json.load(response)
needle = input['needle']
needlePosition = -1
haystackSize = len(input['haystack'])
for i in range(0, haystackSize):
    if needle == input['haystack'][i]:
        # found the needle in the haystack
        needlePosition = i
        break

# make sure nothing went wrong before attempting to validate
if needlePosition != -1:
    # return the needles position in the haystack to this url for validation
    targetURL = 'http://challenge.code2040.org/api/haystack/validate'
    dictionary = {'token': '30e2d792d1001d661697aed566e0341a', 'needle': needlePosition}
    create_HTTP_request(targetURL, dictionary)

else:
    print 'ERROR: The needle was not found in the haystack'
