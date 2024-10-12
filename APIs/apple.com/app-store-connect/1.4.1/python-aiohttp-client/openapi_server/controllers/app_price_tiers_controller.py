from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_price_points_response import AppPricePointsResponse
from openapi_server.models.app_price_tier_response import AppPriceTierResponse
from openapi_server.models.app_price_tiers_response import AppPriceTiersResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_price_tiers_get_collection(request: web.Request, filter_id=None, fields_app_price_tiers=None, limit=None, include=None, fields_app_price_points=None, limit_price_points=None) -> web.Response:
    """app_price_tiers_get_collection

    

    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param fields_app_price_tiers: the fields to include for returned resources of type appPriceTiers
    :type fields_app_price_tiers: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_app_price_points: the fields to include for returned resources of type appPricePoints
    :type fields_app_price_points: List[str]
    :param limit_price_points: maximum number of related pricePoints returned (when they are included)
    :type limit_price_points: int

    """
    return web.Response(status=200)


async def app_price_tiers_get_instance(request: web.Request, id, fields_app_price_tiers=None, include=None, fields_app_price_points=None, limit_price_points=None) -> web.Response:
    """app_price_tiers_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_price_tiers: the fields to include for returned resources of type appPriceTiers
    :type fields_app_price_tiers: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_app_price_points: the fields to include for returned resources of type appPricePoints
    :type fields_app_price_points: List[str]
    :param limit_price_points: maximum number of related pricePoints returned (when they are included)
    :type limit_price_points: int

    """
    return web.Response(status=200)


async def app_price_tiers_price_points_get_to_many_related(request: web.Request, id, fields_app_price_points=None, limit=None) -> web.Response:
    """app_price_tiers_price_points_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_price_points: the fields to include for returned resources of type appPricePoints
    :type fields_app_price_points: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)
