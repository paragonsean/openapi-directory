from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_creditmemo_comment_repository_v1_save_post_request import SalesCreditmemoCommentRepositoryV1SavePostRequest
from openapi_server.models.sales_data_creditmemo_comment_interface import SalesDataCreditmemoCommentInterface
from openapi_server.models.sales_data_creditmemo_comment_search_result_interface import SalesDataCreditmemoCommentSearchResultInterface
from openapi_server import util


async def sales_creditmemo_comment_repository_v1_save_post(request: web.Request, id, body=None) -> web.Response:
    """creditmemo/{id}/comments

    Performs persist operations for a specified entity.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SalesCreditmemoCommentRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)


async def sales_creditmemo_management_v1_get_comments_list_get(request: web.Request, id) -> web.Response:
    """creditmemo/{id}/comments

    Lists comments for a specified credit memo.

    :param id: The credit memo ID.
    :type id: int

    """
    return web.Response(status=200)
