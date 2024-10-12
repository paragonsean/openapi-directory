from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success
from openapi_server import util


async def get_air_traffic(request: web.Request, origin_city_code, period, max=None, fields=None, page_limit=None, page_offset=None, sort=None) -> web.Response:
    """Returns a list of air traffic reports.

    

    :param origin_city_code: Code for the origin city following IATA standard ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)). - e.g. BOS for Boston
    :type origin_city_code: str
    :param period: period when consumers are traveling. * It can be a month only.  * ISO format must be used - e.g. 2015-05.  * Period ranges are not supported.  * Only periods from 2011-01 up to previous month are valid.  * Future dates are not supported. 
    :type period: str
    :param max: maximum number of destinations in the response. Default value is 10 and maximum value is 50.
    :type max: 
    :param fields: list of attributes desired in the response or list of attributes to remove from the response (with \&quot;-\&quot; before fields)  * The attributes names must contain the whole path (except resource name) e.g. travelers
    :type fields: str
    :param page_limit: maximum items in one page
    :type page_limit: int
    :param page_offset: start index of the requested page
    :type page_offset: int
    :param sort: defines on which attribute the sorting will be done: * analytics.flights.score - sort destinations by flights score (decreasing) * analytics.travelers.score - sort destination by traveler&#39;s score (decreasing) 
    :type sort: str

    """
    return web.Response(status=200)
