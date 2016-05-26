from lxml import etree
import requests


# #domain = "http://www.flyniki.com/start.php"
# domain = "http://www.flyniki.com/en/booking/flight/vacancy.php?departure=CEK&destination=PEK&outboundDate=2016-06-16&returnDate=2016-06-16&oneway=0&openDateOverview=0&adultCount=1&childCount=0&infantCount=0"
# resp_one = requests.get(domain, stream=True)
# b = resp_one.text
# print b

def to_start(Departure, Destination, OutboundDate, ReturnDate=""):
    domain = "http://www.flyniki.com/en/booking/flight/vacancy.php?departure=CEK&destination=PEK&outboundDate=2016-06-16&returnDate=&oneway=1&openDateOverview=0&adultCount=1&childCount=0&infantCount=0"
    resp_one = requests.get(domain, stream=True)
    ssid_url = resp_one.url
    return resp_one.url


print to_start("PEK", "DME", "2016-06-16", "2016-06-24")

# Location: http://www.flyniki.com/en/booking/flight/vacancy.php?departure=CEK&destination=PEK&outboundDate=2016-06-16&returnDate=&oneway=1&openDateOverview=0&adultCount=1&childCount=0&infantCount=0
