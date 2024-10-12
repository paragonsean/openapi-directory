from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_domain_cert_v4 import MessagingV1DomainCertV4
from openapi_server import util


async def delete_domain_cert_v4(request: web.Request, domain_sid) -> web.Response:
    """delete_domain_cert_v4

    

    :param domain_sid: Unique string used to identify the domain that this certificate should be associated with.
    :type domain_sid: str

    """
    return web.Response(status=200)


async def fetch_domain_cert_v4(request: web.Request, domain_sid) -> web.Response:
    """fetch_domain_cert_v4

    

    :param domain_sid: Unique string used to identify the domain that this certificate should be associated with.
    :type domain_sid: str

    """
    return web.Response(status=200)


async def update_domain_cert_v4(request: web.Request, domain_sid, tls_cert) -> web.Response:
    """update_domain_cert_v4

    

    :param domain_sid: Unique string used to identify the domain that this certificate should be associated with.
    :type domain_sid: str
    :param tls_cert: Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.
    :type tls_cert: str

    """
    return web.Response(status=200)
