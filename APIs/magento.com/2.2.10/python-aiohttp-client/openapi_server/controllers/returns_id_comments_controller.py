from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rma_comment_management_v1_add_comment_post_request import RmaCommentManagementV1AddCommentPostRequest
from openapi_server.models.rma_data_comment_search_result_interface import RmaDataCommentSearchResultInterface
from openapi_server import util


async def rma_comment_management_v1_add_comment_post(request: web.Request, id, body=None) -> web.Response:
    """returns/{id}/comments

    Add comment

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RmaCommentManagementV1AddCommentPostRequest.from_dict(body)
    return web.Response(status=200)


async def rma_comment_management_v1_comments_list_get(request: web.Request, id) -> web.Response:
    """returns/{id}/comments

    Comments list

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
