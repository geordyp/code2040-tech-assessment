import json
import urllib2

# registration endpoint
targetURL = 'http://challenge.code2040.org/api/register'

# the registration endpoint expects a JSON dictionary with two keys, token and github
registrationKeys = {'token': '30e2d792d1001d661697aed566e0341a',
                    'github': 'https://github.com/geordyp/code2040-tech-assessment'}

# http://www.stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json
request = urllib2.Request(targetURL)
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request, json.dumps(registrationKeys))
