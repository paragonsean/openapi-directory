from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def rma_track_management_v1_get_shipping_label_pdf_get(request: web.Request, id) -> web.Response:
    """returns/{id}/labels

    Get shipping label int the PDF format

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
