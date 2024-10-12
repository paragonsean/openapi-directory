from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_invoice_comment_interface import SalesDataInvoiceCommentInterface
from openapi_server.models.sales_invoice_comment_repository_v1_save_post_request import SalesInvoiceCommentRepositoryV1SavePostRequest
from openapi_server import util


async def sales_invoice_comment_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """invoices/comments

    Performs persist operations for a specified invoice comment.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesInvoiceCommentRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
