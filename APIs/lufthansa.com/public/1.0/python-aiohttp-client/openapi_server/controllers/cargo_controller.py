from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def cargo_get_route_from_date_product_code_by_origin_and_destination_get(request: web.Request, origin, destination, from_date, product_code, accept) -> web.Response:
    """Retrieve all flights

    Retrieve a list of all possible flights (both direct and connecting) between two airports on a given date. Routes are available for today and up to days in the future.

    :param origin: Departure Airport : 3-letter IATA airport code, e.g. FRA.
    :type origin: str
    :param destination: Arrival airport : 3-letter IATA airport code, e.g. HKG.
    :type destination: str
    :param from_date: Departure date in the local time of the departure airport. Based on LAT (Latest Acceptance Time). format : yyyy-MM-dd eg : 2017-07-15
    :type from_date: str
    :param product_code: Product code for requested service and specials : 3-letter eg: YNZ
    :type product_code: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str

    """
    return web.Response(status=200)


async def cargo_shipment_tracking_by_awb_prefix_and_awb_number_get(request: web.Request, a_wb_prefix, a_wb_number, accept) -> web.Response:
    """Shipment Tracking

    With this tracking service you can easily retrieve your shipment or flight status information.

    :param a_wb_prefix: aWBPrefix : Represents the airline that is the owner of this AWB, i.e. \&quot;020\&quot; &#x3D; Lufthansa Cargo, format : [0-9]{3} e.g. 020
    :type a_wb_prefix: str
    :param a_wb_number: aWBNumber : The Air Waybill Number , format : [0-9]{8} e.g. 08002050
    :type a_wb_number: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str

    """
    return web.Response(status=200)
