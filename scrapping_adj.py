import requests

# what is the quote?
options = {'Departure': 'WAW',
           'Destination': 'SOF',
           'Outbound': '2016-06-16',
           "ReturnDate": ""}

# processing
def to_start(kwargs):
    # return flights
    if(len(kwargs["ReturnDate"])>0):
        domain = "http://www.flyniki.com/en/booking/flight/vacancy.php?departure={Departure}" \
             "&destination={Destination}" \
             "&outboundDate={Outbound}" \
             "&returnDate={ReturnDate}&oneway=0" \
             "&openDateOverview=0&adultCount=1&childCount=0&infantCount=0".format(**kwargs)
    # oneway flights
    elif(len(kwargs["ReturnDate"])==0):
        domain = "http://www.flyniki.com/en/booking/flight/vacancy.php?departure={Departure}" \
             "&destination={Destination}" \
             "&outboundDate={Outbound}" \
             "&returnDate={ReturnDate}&oneway=1" \
             "&openDateOverview=0&adultCount=1&childCount=0&infantCount=0".format(**kwargs)
    resp_one = requests.get(domain, stream=True, allow_redirects=False)
    return resp_one.headers["Set-Cookie"]


# cookies_list = launch.cookies
# second = requests.get("http://www.flyniki.com" + launch.headers['Location'], allow_redirects=False)
# launch = requests.get(second.url, allow_redirects=False, cookies=cookies_list)
# return launch.json()

print to_start(options)

# Location: http://www.flyniki.com/en/booking/flight/vacancy.php?departure=PEK&destination=LED&outboundDate=2016-06-16&returnDate=&oneway=1&openDateOverview=0&adultCount=1&childCount=0&infantCount=0
