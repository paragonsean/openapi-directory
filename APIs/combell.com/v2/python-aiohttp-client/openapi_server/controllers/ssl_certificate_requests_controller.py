from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_ssl_certificate_request import CreateSslCertificateRequest
from openapi_server.models.ssl_certificate_request import SslCertificateRequest
from openapi_server.models.ssl_certificate_request_detail import SslCertificateRequestDetail
from openapi_server import util


async def add_ssl_certificate_request(request: web.Request, body=None) -> web.Response:
    """Add a SSL certificate request

    Executing this method causes the purchase of a paying product.&lt;br /&gt;  Log on to our website to see your current (renewal) prices or contact our Sales department.&lt;br /&gt;  Please note that promotional pricing does not apply for purchases made through our API.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateSslCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def get_ssl_certificate_request(request: web.Request, id) -> web.Response:
    """Detail of a SSL certificate request

    

    :param id: The id of the certificate request.
    :type id: int

    """
    return web.Response(status=200)


async def get_ssl_certificate_requests(request: web.Request, skip=None, take=None) -> web.Response:
    """Overview of SSL certificate requests

    

    :param skip: The number of items to skip in the resultset.
    :type skip: int
    :param take: The number of items to return in the resultset. The returned count can be equal or less than this number.
    :type take: int

    """
    return web.Response(status=200)


async def verify_ssl_certificate_request_domain_validations(request: web.Request, id) -> web.Response:
    """Verify the SSL certificate request domain validations

    

    :param id: The id of the certificate request.
    :type id: int

    """
    return web.Response(status=200)
