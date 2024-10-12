from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.promotions_entity import PromotionsEntity
from openapi_server import util


async def fetch_all_events_promotions(request: web.Request, event_id, label=None, from_date=None, to_date=None, type=None, family=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all promotions for one event

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param label: Find only the promotions whose label contains this value.
    :type label: str
    :param from_date: Find only the promotions starting after this date.
    :type from_date: str
    :param to_date: Find only the promotions ending before this date.
    :type to_date: str
    :param type: Find only the promotions whose type is equal to this value.
    :type type: str
    :param family: Find only the promotions whose family is equal to this value.
    :type family: str
    :param sort: Sort the promotions in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def fetch_all_promotions(request: web.Request, label=None, from_date=None, to_date=None, type=None, family=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all promotions

    

    :param label: Find only the promotions whose label contains this value.
    :type label: str
    :param from_date: Find only the promotions starting after this date.
    :type from_date: str
    :param to_date: Find only the promotions ending before this date.
    :type to_date: str
    :param type: Find only the promotions whose type is equal to this value.
    :type type: str
    :param family: Find only the promotions whose family is equal to this value.
    :type family: str
    :param sort: Sort the promotions in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def fetch_all_series_promotions(request: web.Request, series_id, label=None, from_date=None, to_date=None, type=None, family=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all promotions for one series

    

    :param series_id: ID of the targeted series.
    :type series_id: int
    :param label: Find only the promotions whose label contains this value.
    :type label: str
    :param from_date: Find only the promotions starting after this date.
    :type from_date: str
    :param to_date: Find only the promotions ending before this date.
    :type to_date: str
    :param type: Find only the promotions whose type is equal to this value.
    :type type: str
    :param family: Find only the promotions whose family is equal to this value.
    :type family: str
    :param sort: Sort the promotions in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def fetch_one_promotion(request: web.Request, promotion_id, accept_language=None) -> web.Response:
    """Get one promotion by ID

    

    :param promotion_id: ID of the targeted promotion.
    :type promotion_id: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)
