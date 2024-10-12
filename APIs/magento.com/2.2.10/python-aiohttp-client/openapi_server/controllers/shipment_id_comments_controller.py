from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_shipment_comment_interface import SalesDataShipmentCommentInterface
from openapi_server.models.sales_data_shipment_comment_search_result_interface import SalesDataShipmentCommentSearchResultInterface
from openapi_server.models.sales_shipment_comment_repository_v1_save_post_request import SalesShipmentCommentRepositoryV1SavePostRequest
from openapi_server import util


async def sales_shipment_comment_repository_v1_save_post(request: web.Request, id, body=None) -> web.Response:
    """shipment/{id}/comments

    Performs persist operations for a specified shipment comment.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SalesShipmentCommentRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)


async def sales_shipment_management_v1_get_comments_list_get(request: web.Request, id) -> web.Response:
    """shipment/{id}/comments

    Lists comments for a specified shipment.

    :param id: The shipment ID.
    :type id: int

    """
    return web.Response(status=200)
