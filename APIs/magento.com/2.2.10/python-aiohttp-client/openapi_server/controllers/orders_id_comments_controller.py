from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_order_status_history_search_result_interface import SalesDataOrderStatusHistorySearchResultInterface
from openapi_server.models.sales_order_management_v1_add_comment_post_request import SalesOrderManagementV1AddCommentPostRequest
from openapi_server import util


async def sales_order_management_v1_add_comment_post(request: web.Request, id, body=None) -> web.Response:
    """orders/{id}/comments

    Adds a comment to a specified order.

    :param id: The order ID.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SalesOrderManagementV1AddCommentPostRequest.from_dict(body)
    return web.Response(status=200)


async def sales_order_management_v1_get_comments_list_get(request: web.Request, id) -> web.Response:
    """orders/{id}/comments

    Lists comments for a specified order.

    :param id: The order ID.
    :type id: int

    """
    return web.Response(status=200)
