from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_data_attachment_content_interface import NegotiableQuoteDataAttachmentContentInterface
from openapi_server import util


async def negotiable_quote_attachment_content_management_v1_get_get(request: web.Request, attachment_ids) -> web.Response:
    """negotiableQuote/attachmentContent

    Returns content for one or more files attached on the quote comment.

    :param attachment_ids: 
    :type attachment_ids: List[int]

    """
    return web.Response(status=200)
