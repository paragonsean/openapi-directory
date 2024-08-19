from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.document_block_list import DocumentBlockList
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse
from openapi_server import util


async def list_document_block(request: web.Request, page=None, per_page=None) -> web.Response:
    """List all document blocks

    Returns a list of your document blocks. The document blocks are returned sorted by creation date, with the most recent document blocks appearing first.

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)
