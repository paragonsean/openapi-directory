from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.series_entity import SeriesEntity
from openapi_server import util


async def fetch_all_series(request: web.Request, label=None, from_date=None, to_date=None, type=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all series

    

    :param label: Find only the venues whose label contains this value.
    :type label: str
    :param from_date: Find only the series starting after this date.
    :type from_date: str
    :param to_date: Find only the series ending before this date.
    :type to_date: str
    :param type: Find only the series whose type is equal to this value.
    :type type: str
    :param sort: Sort the series in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def fetch_one_series(request: web.Request, series_id, accept_language=None) -> web.Response:
    """Get one series by ID

    

    :param series_id: ID of the targeted series.
    :type series_id: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)
