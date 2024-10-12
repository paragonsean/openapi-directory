from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.sni_certificate import SniCertificate
from openapi_server import util


async def provision_site_tls_certificate(request: web.Request, site_id, certificate=None, key=None, ca_certificates=None) -> web.Response:
    """provision_site_tls_certificate

    

    :param site_id: 
    :type site_id: str
    :param certificate: 
    :type certificate: str
    :param key: 
    :type key: str
    :param ca_certificates: 
    :type ca_certificates: str

    """
    return web.Response(status=200)


async def show_site_tls_certificate(request: web.Request, site_id) -> web.Response:
    """show_site_tls_certificate

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)
