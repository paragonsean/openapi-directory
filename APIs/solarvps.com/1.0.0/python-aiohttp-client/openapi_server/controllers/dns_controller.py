from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def dns_domain_add_post(request: web.Request, domain, name, type, content, ttl, prio) -> web.Response:
    """Add dns record for given domain

    You can try example.com below. Types allowed are: A CNAME NS TXT MX SRV SPF

    :param domain: Domain you want to add records for
    :type domain: str
    :param name: Fully qualified DNS name
    :type name: str
    :param type: Type of DNS record
    :type type: str
    :param content: Content for DNS record
    :type content: str
    :param ttl: Time To Live for DNS record
    :type ttl: str
    :param prio: Priority of DNS record
    :type prio: str

    """
    return web.Response(status=200)


async def dns_domain_delete_post(request: web.Request, domain, id) -> web.Response:
    """Delete dns record for a given domain

    Shows all your records for a specific domain. You can try example.com below.

    :param domain: Domain name you want to get records for
    :type domain: str
    :param id: Id of the DNS Record
    :type id: str

    """
    return web.Response(status=200)


async def dns_domain_get(request: web.Request, domain) -> web.Response:
    """View all your records for a given domain

    Shows all your records for a specific domain. You can try example.com below.

    :param domain: Domain name you want to get records for
    :type domain: str

    """
    return web.Response(status=200)


async def dns_domain_update_post(request: web.Request, domain, id, name=None, type=None, content=None, ttl=None, prio=None) -> web.Response:
    """Update dns record for a given domain

    You can try example.com below.

    :param domain: Domain name to add record under
    :type domain: str
    :param id: Id of DNS record
    :type id: str
    :param name: Fully qualified name for the DNS record
    :type name: str
    :param type: Type for DNS record
    :type type: str
    :param content: Content for the DNS Record
    :type content: str
    :param ttl: Time To Live for DNS record
    :type ttl: str
    :param prio: Priority of the DNS record
    :type prio: str

    """
    return web.Response(status=200)
