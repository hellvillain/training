import requests
import sys
from lxml import html


def changed_string(str):
    return (str[-4:] + str[2:-4] + str[:2]).replace("/", "-")


def get_prices(origin, destination, outbound_date, return_date=None):

    values = {"market": "GB",
              "language": "en",
              "bookingmask_widget_id": "bookingmask-widget-stageoffer",
              "bookingmask_widget_dateformat": "dd/mm/yy",
              "departure": str(origin).capitalize(),
              "destination": str(destination).capitalize(),
              "outboundDate": str(outbound_date),
              "adultCount": "1",
              "childCount": "0",
              "infantCount": "0",
              "submitSearch": "",
              }

    form_data = {" _ajax[templates][]": ["main", "priceoverview", "infos", "flightinfo"],
                 "_ajax[requestParams][departure]": str(origin),
                 "_ajax[requestParams][destination]": str(destination),
                 "_ajax[requestParams][returnDeparture]": str(destination),
                 "_ajax[requestParams][returnDestination]": str(origin),
                 "_ajax[requestParams][outboundDate]": changed_string(outbound_date),
                 "_ajax[requestParams][adultCount]": "1",
                 "_ajax[requestParams][childCount]": "0",
                 "_ajax[requestParams][infantCount]": "0",
                 "_ajax[requestParams][openDateOverview]": "",
                 }

    if return_date == None:
        values["oneway"] = "on"
        form_data["_ajax[requestParams][oneway]"] = "1"
    elif len(return_date) > 0:
        values["returnDate"] = str(return_date)
        form_data["_ajax[requestParams][returnDate]"] = changed_string(return_date)

    domain = "http://www.flyniki.com/en/start.php"

    # sending responses
    virgin = requests.Session()
    virgin.get(domain)
    second = virgin.post(domain, data=values)
    third = virgin.post(second.url, data=form_data)

    # json processing
    data_unicode = third.json()
    general_tree = html.fromstring(data_unicode['templates']['main'])
    departure = general_tree.xpath(".//*[@class=\"outbound block\"]//div[@class=\"vacancy_route\"]/text()")
    destination = general_tree.xpath(".//*[@class=\"return block\"]//div[@class=\"vacancy_route\"]/text()")
    prices = general_tree.xpath(".//div[@class=\"current\"]/span/text()")
    if return_date == None:
        return departure, prices
    elif len(return_date) > 0:
        return departure, destination, prices


# print get_prices("warsaw", "sofia", "15/06/2016", "23/06/2016")

def main():

    args = sys.argv[1:]

    # if empty
    if not args:
        print 'format of query: origin_city destination_city outboundDate(\"dd/mm/yy\") returnDate(\"dd/mm/yy\"))'
        sys.exit(1)

    if len(args) == 4:
        print "flights: ", get_prices(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        sys.exit()
    else:
        print "flights: ", get_prices(sys.argv[1], sys.argv[2], sys.argv[3])
        sys.exit()

if __name__ == '__main__':
    main()
