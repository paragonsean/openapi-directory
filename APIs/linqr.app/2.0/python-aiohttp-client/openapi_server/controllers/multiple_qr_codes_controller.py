from typing import List, Dict
from aiohttp import web

from openapi_server.models.auto_qr_code_batch import AutoQRCodeBatch
from openapi_server.models.generic_error import GenericError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def qr_code_batch_batch_qrcode_post(request: web.Request, body) -> web.Response:
    """QR Code Batch

    This endpoint allows you to generate an archive containing multiple QR Codes with a single request. The endpoint response is the archive containing the generated image files and &#x60;items.json&#x60; file which is a record of the specifications of each of the files in the archive.

    :param body: 
    :type body: dict | bytes

    """
    body = AutoQRCodeBatch.from_dict(body)
    return web.Response(status=200)
