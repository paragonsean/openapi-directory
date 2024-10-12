from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_service_point_by_id_response_body import GetServicePointByIdResponseBody
from openapi_server.models.get_service_points_request import GetServicePointsRequest
from openapi_server.models.list_service_points_response_body import ListServicePointsResponseBody
from openapi_server import util


async def service_points_get_by_id(request: web.Request, carrier_code, country_code, service_point_id) -> web.Response:
    """Get Service Point By ID

    Returns a carrier service point by using the service_point_id

    :param carrier_code: Carrier code
    :type carrier_code: str
    :param country_code: A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1) 
    :type country_code: str
    :param service_point_id: 
    :type service_point_id: str

    """
    return web.Response(status=200)


async def service_points_list(request: web.Request, body) -> web.Response:
    """List Service Points

    List carrier service points by location

    :param body: 
    :type body: dict | bytes

    """
    body = GetServicePointsRequest.from_dict(body)
    return web.Response(status=200)
