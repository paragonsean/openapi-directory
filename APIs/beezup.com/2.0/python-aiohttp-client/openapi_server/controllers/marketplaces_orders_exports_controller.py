from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.export_order_list_request import ExportOrderListRequest
from openapi_server.models.order_exportations import OrderExportations
from openapi_server import util


async def export_orders(request: web.Request, body) -> web.Response:
    """Request a new Order report exportation to be generated

    A new file will be generated containing a summary of all the Orders matching the requested filter settings.

    :param body: 
    :type body: dict | bytes

    """
    body = ExportOrderListRequest.from_dict(body)
    return web.Response(status=200)


async def get_order_exportations(request: web.Request, page_number, page_size, store_id, if_none_match=None) -> web.Response:
    """Get a paginated list of Order report exportations

    

    :param page_number: The page number you want to get
    :type page_number: int
    :param page_size: The entry count you want to get
    :type page_size: int
    :param store_id: The store identifier to regroup the order exportations
    :type store_id: str
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)
