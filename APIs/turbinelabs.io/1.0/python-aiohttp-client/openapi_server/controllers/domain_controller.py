from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain_create import DomainCreate
from openapi_server.models.domain_result import DomainResult
from openapi_server.models.error import Error
from openapi_server.models.multi_domain_result import MultiDomainResult
from openapi_server import util


async def domain_domain_key_delete(request: web.Request, domain_key, checksum) -> web.Response:
    """delete domain

    Delete an existing domain

    :param domain_key: the domain key
    :type domain_key: str
    :param checksum: the current checksum of the domain to be deleted
    :type checksum: str

    """
    return web.Response(status=200)


async def domain_domain_key_get(request: web.Request, domain_key) -> web.Response:
    """get domain

    Get details for a single domain

    :param domain_key: the domain key
    :type domain_key: str

    """
    return web.Response(status=200)


async def domain_get(request: web.Request, filters=None) -> web.Response:
    """get domains

    Get a list of domains

    :param filters: A JSON encoded array of DomainFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any DomainFilter will be included. 
    :type filters: str

    """
    return web.Response(status=200)


async def domain_post(request: web.Request, domain) -> web.Response:
    """create domain

    Create a new domain

    :param domain: the domain to create
    :type domain: dict | bytes

    """
    domain = DomainCreate.from_dict(domain)
    return web.Response(status=200)
