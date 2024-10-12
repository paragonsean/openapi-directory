from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.venues_entity import VenuesEntity
from openapi_server import util


async def fetch_all_venues(request: web.Request, label=None, city=None, country_code=None, type=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all venues

    

    :param label: Find only the venues whose label contains this value.
    :type label: str
    :param city: Find only the venues whose city contains this value.
    :type city: str
    :param country_code: Find only the venues whose country_code is equal to this value.
    :type country_code: str
    :param type: Find only the venues whose type is equal to this value.
    :type type: str
    :param sort: Sort the venues in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)


async def fetch_one_venue(request: web.Request, venue_id, accept_language=None) -> web.Response:
    """Get one venue by ID

    

    :param venue_id: ID of the targeted venue.
    :type venue_id: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)
