from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.prediction import Prediction
from openapi_server import util


async def get_flight_delay_prediction(request: web.Request, origin_location_code, destination_location_code, departure_date, departure_time, arrival_date, arrival_time, aircraft_code, carrier_code, flight_number, duration) -> web.Response:
    """Return the delay segment where the flight is likely to lay.

    

    :param origin_location_code: city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler is departing, e.g. PAR for Paris
    :type origin_location_code: str
    :param destination_location_code: city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris
    :type destination_location_code: str
    :param departure_date: the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
    :type departure_date: str
    :param departure_time: local time relative to originLocationCode on which the traveler will depart from the origin. Time respects ISO 8601 standard. e.g. 13:22:00
    :type departure_time: str
    :param arrival_date: the date on which the traveler will arrive to the destination from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
    :type arrival_date: str
    :param arrival_time: local time relative to destinationLocationCode on which the traveler will arrive to destination. Time respects ISO 8601 standard. e.g. 13:22:00
    :type arrival_time: str
    :param aircraft_code: IATA aircraft code (http://www.flugzeuginfo.net/table_accodes_iata_en.php)
    :type aircraft_code: str
    :param carrier_code: airline / carrier code
    :type carrier_code: str
    :param flight_number: flight number as assigned by the carrier
    :type flight_number: str
    :param duration: flight duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
    :type duration: str

    """
    departure_date = util.deserialize_date(departure_date)
    arrival_date = util.deserialize_date(arrival_date)
    return web.Response(status=200)
