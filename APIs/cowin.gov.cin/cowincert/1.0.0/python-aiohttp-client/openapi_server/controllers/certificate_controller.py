from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_request import CertificateRequest
from openapi_server import util


async def get_certificate_pdf(request: web.Request, body) -> web.Response:
    """Download the certificate in pdf format

    

    :param body: 
    :type body: dict | bytes

    """
    body = CertificateRequest.from_dict(body)
    return web.Response(status=200)
