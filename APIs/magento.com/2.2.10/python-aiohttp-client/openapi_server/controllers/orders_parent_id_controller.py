from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_order_address_interface import SalesDataOrderAddressInterface
from openapi_server.models.sales_order_address_repository_v1_save_put_request import SalesOrderAddressRepositoryV1SavePutRequest
from openapi_server import util


async def sales_order_address_repository_v1_save_put(request: web.Request, parent_id, body=None) -> web.Response:
    """orders/{parent_id}

    Performs persist operations for a specified order address.

    :param parent_id: 
    :type parent_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SalesOrderAddressRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
