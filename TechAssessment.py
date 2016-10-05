import json
import urllib2

# my API token: 30e2d792d1001d661697aed566e0341a

# this endpoint will return a string that needs to be reverse
targetURL = 'http://challenge.code2040.org/api/reverse'
dictionary = {'token': '30e2d792d1001d661697aed566e0341a'}

request = urllib2.Request(targetURL)
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request, json.dumps(dictionary))

# reverse the input string
input = response.read(100)
output = ''
inputLength = len(input)
for i in range(0, inputLength):
    output += input[(inputLength - 1) - i]

# return the resulting string to this url for validation
targetURL = 'http://challenge.code2040.org/api/reverse/validate'
dictionary = {'token': '30e2d792d1001d661697aed566e0341a', 'string': output}

request = urllib2.Request(targetURL)
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request, json.dumps(dictionary))
