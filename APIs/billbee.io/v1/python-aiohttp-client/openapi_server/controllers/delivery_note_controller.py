from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def order_api_create_delivery_note_0(request: web.Request, id, include_pdf=None, send_to_cloud_id=None) -> web.Response:
    """Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

    

    :param id: The internal billbee id of the order
    :type id: int
    :param include_pdf: If true, the PDF is included in the response as base64 encoded string
    :type include_pdf: bool
    :param send_to_cloud_id: Optionally specify the id of a billbee connected cloud device to send the pdf to
    :type send_to_cloud_id: int

    """
    return web.Response(status=200)
