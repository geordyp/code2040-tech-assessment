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

# numToStr() takes a number and returns the number as a string
# prepending a 0 if the number is only 1 digit
#
# @param {Integer} num
# @return {String} num
def numToStr(num):
    if (num < 10):
        return '0' + str(num)
    return str(num)

# this endpoint will return a JSON with keys 'datestamp' and 'interval'
targetURL = 'http://challenge.code2040.org/api/dating'
dictionary = {'token': '30e2d792d1001d661697aed566e0341a'}
response = create_HTTP_request(targetURL, dictionary)

# {'datestamp': ---, 'interval': ---}
input = json.load(response)

# ISO 8601 YYYY-MM-DDThh:mm:ssZ
datestamp = input['datestamp']
year = int(datestamp[0:4])
month = int(datestamp[5:7])
day = int(datestamp[8:10])
hour = int(datestamp[11:13])
minute = int(datestamp[14:16])
second = int(datestamp[17:19])

# seconds
interval = input['interval']
addSeconds = interval%60
addMinutes = (interval/60)%60
addHours = (interval/60/60)%24
addDays = interval/60/60/24

# set second
second += addSeconds
if second > 59:
    second = second%60
    minute += 1

# set minute
minute += addMinutes
if minute > 59:
    minute = minute%60
    hour += 1

# set hour
hour += addHours
if hour > 23:
    hour = hour%24
    day += 1

# set day
day += addDays
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    # month with 31 days
    if day > 31:
        day = day%31
        month += 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    # month with 30 days
    if day > 30:
        day = day%30
        month += 1
elif month == 2:
    # month with 28 or 29 days
    if year%4 == 0:
        if day > 29:
            day = day%29
            month += 1
    else:
        if day > 28:
            day = day%28
            month += 1

# check month
if month > 12:
    month = month%12
    year += 1

output = numToStr(year) + '-' + numToStr(month) + '-' + numToStr(day) + 'T' + numToStr(hour) + ':' + numToStr(minute) + ':' + numToStr(second) + 'Z'

# return the list of words that DON'T start with the given prefix
targetURL = 'http://challenge.code2040.org/api/dating/validate'
dictionary = {'token': '30e2d792d1001d661697aed566e0341a', 'datestamp': output}
create_HTTP_request(targetURL, dictionary)
