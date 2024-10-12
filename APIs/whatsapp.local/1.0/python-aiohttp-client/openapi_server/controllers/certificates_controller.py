from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def delete_webhook_ca_certificate(request: web.Request, ) -> web.Response:
    """Delete Webhook CA Certificate

    


    """
    return web.Response(status=200)


async def download_ca_certificate(request: web.Request, ) -> web.Response:
    """Download-CA-Certificate

    


    """
    return web.Response(status=200)


async def download_webhook_ca_certificate(request: web.Request, ) -> web.Response:
    """Download Webhook CA Certificate

    


    """
    return web.Response(status=200)


async def upload_certificate(request: web.Request, body=None) -> web.Response:
    """Upload-Certificate

    

    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def upload_webhook_ca_certificate(request: web.Request, body=None) -> web.Response:
    """Upload Webhook CA Certificate

    

    :param body: 
    :type body: str

    """
    return web.Response(status=200)
