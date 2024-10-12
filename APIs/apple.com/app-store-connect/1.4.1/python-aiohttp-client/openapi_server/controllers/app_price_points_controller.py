from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_price_point_response import AppPricePointResponse
from openapi_server.models.app_price_points_response import AppPricePointsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.territory_response import TerritoryResponse
from openapi_server import util


async def app_price_points_get_collection(request: web.Request, filter_price_tier=None, filter_territory=None, fields_app_price_points=None, limit=None, include=None, fields_territories=None) -> web.Response:
    """app_price_points_get_collection

    

    :param filter_price_tier: filter by id(s) of related &#39;priceTier&#39;
    :type filter_price_tier: List[str]
    :param filter_territory: filter by id(s) of related &#39;territory&#39;
    :type filter_territory: List[str]
    :param fields_app_price_points: the fields to include for returned resources of type appPricePoints
    :type fields_app_price_points: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_territories: the fields to include for returned resources of type territories
    :type fields_territories: List[str]

    """
    return web.Response(status=200)


async def app_price_points_get_instance(request: web.Request, id, fields_app_price_points=None, include=None, fields_territories=None) -> web.Response:
    """app_price_points_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_price_points: the fields to include for returned resources of type appPricePoints
    :type fields_app_price_points: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_territories: the fields to include for returned resources of type territories
    :type fields_territories: List[str]

    """
    return web.Response(status=200)


async def app_price_points_territory_get_to_one_related(request: web.Request, id, fields_territories=None) -> web.Response:
    """app_price_points_territory_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_territories: the fields to include for returned resources of type territories
    :type fields_territories: List[str]

    """
    return web.Response(status=200)
