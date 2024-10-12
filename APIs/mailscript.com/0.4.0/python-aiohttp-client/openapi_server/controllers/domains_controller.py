from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_domain_request import AddDomainRequest
from openapi_server.models.check_domain_verify import CheckDomainVerify
from openapi_server.models.domain_response import DomainResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_domains_response import GetAllDomainsResponse
from openapi_server import util


async def add_domain(request: web.Request, body) -> web.Response:
    """Claim a new Domain

    

    :param body: Domain body
    :type body: dict | bytes

    """
    body = AddDomainRequest.from_dict(body)
    return web.Response(status=200)


async def check_domain_verify(request: web.Request, domain) -> web.Response:
    """Check a new Domain

    

    :param domain: Full Top-level domain name
    :type domain: str

    """
    return web.Response(status=200)


async def get_all_domains(request: web.Request, ) -> web.Response:
    """Get all domains you have access to

    


    """
    return web.Response(status=200)


async def get_domain_verify(request: web.Request, domain) -> web.Response:
    """Get domain verification

    

    :param domain: Full Top-level domain name
    :type domain: str

    """
    return web.Response(status=200)


async def remove_domain_verify(request: web.Request, domain) -> web.Response:
    """Remove a domain

    

    :param domain: Full Top-level domain name
    :type domain: str

    """
    return web.Response(status=200)
