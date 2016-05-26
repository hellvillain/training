from lxml import etree
import requests


# #domain = "http://www.flyniki.com/start.php"
# domain = "http://www.flyniki.com/en/booking/flight/vacancy.php?departure=CEK&destination=PEK&outboundDate=2016-06-16&returnDate=2016-06-16&oneway=0&openDateOverview=0&adultCount=1&childCount=0&infantCount=0"
# resp_one = requests.get(domain, stream=True)
# b = resp_one.text
# print b
options = {'Departure': 'PEK',
           'Destination': 'LED',
           'Outbound': '2016-06-16',
           "ReturnDate": ""}


def to_start(kwargs):
    if(len(kwargs["ReturnDate"])>0):
        domain = "http://www.flyniki.com/en/booking/flight/vacancy.php?departure={Departure}" \
             "&destination={Destination}" \
             "&outboundDate={Outbound}" \
             "&returnDate={ReturnDate}&oneway=0" \
             "&openDateOverview=0&adultCount=1&childCount=0&infantCount=0".format(**kwargs)
    elif(len(kwargs["ReturnDate"])==0):
        domain = "http://www.flyniki.com/en/booking/flight/vacancy.php?departure={Departure}" \
             "&destination={Destination}" \
             "&outboundDate={Outbound}" \
             "&returnDate={ReturnDate}&oneway=1" \
             "&openDateOverview=0&adultCount=1&childCount=0&infantCount=0".format(**kwargs)
    resp_one = requests.get(domain, stream=True)
    ssid_url = resp_one.url
    return resp_one.url


print to_start(options)

# Location: http://www.flyniki.com/en/booking/flight/vacancy.php?departure=CEK&destination=PEK&outboundDate=2016-06-16&returnDate=&oneway=1&openDateOverview=0&adultCount=1&childCount=0&infantCount=0
