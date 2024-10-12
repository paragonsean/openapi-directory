from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_category_list import DocumentCategoryList
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def list_document_categories(request: web.Request, ) -> web.Response:
    """list_document_categories

    Returns document categories


    """
    return web.Response(status=200)
