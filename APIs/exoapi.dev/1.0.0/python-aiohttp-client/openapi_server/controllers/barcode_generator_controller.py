from typing import List, Dict
from aiohttp import web

from openapi_server.models.barcode_generator_post400_response import BarcodeGeneratorPost400Response
from openapi_server.models.barcode_generator_post_request import BarcodeGeneratorPostRequest
from openapi_server import util


async def barcode_generator_post(request: web.Request, body) -> web.Response:
    """barcode_generator_post

    Generate high quality QR code &amp; barcode images in a matter of seconds

    :param body: 
    :type body: dict | bytes

    """
    body = BarcodeGeneratorPostRequest.from_dict(body)
    return web.Response(status=200)
