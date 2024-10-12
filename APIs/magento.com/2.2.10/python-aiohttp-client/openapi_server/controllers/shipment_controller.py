from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_shipment_interface import SalesDataShipmentInterface
from openapi_server.models.sales_shipment_repository_v1_save_post_request import SalesShipmentRepositoryV1SavePostRequest
from openapi_server import util


async def sales_shipment_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """shipment/

    Performs persist operations for a specified shipment.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesShipmentRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
