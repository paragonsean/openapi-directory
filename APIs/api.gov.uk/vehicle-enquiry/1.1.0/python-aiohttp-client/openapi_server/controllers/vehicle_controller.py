from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.vehicle import Vehicle
from openapi_server.models.vehicle_request import VehicleRequest
from openapi_server import util


async def get_vehicle_details_by_registration_number(request: web.Request, x_api_key, body, x_correlation_id=None) -> web.Response:
    """Get vehicle details by registration number

    Returns vehicle details based on registration number

    :param x_api_key: Client Specific API Key
    :type x_api_key: str
    :param body: Registration number of the vehicle to find details for
    :type body: dict | bytes
    :param x_correlation_id: Consumer Correlation ID
    :type x_correlation_id: str

    """
    body = VehicleRequest.from_dict(body)
    return web.Response(status=200)
