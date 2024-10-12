from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def domains_add_post(request: web.Request, domain) -> web.Response:
    """Add domain to be managed by SolarVPS Distributed DNS

    Adds domain to SolarVPS Distributed DNS

    :param domain: Domain to add to SolarVPS Distributed DNS
    :type domain: str

    """
    return web.Response(status=200)


async def domains_delete_post(request: web.Request, domain) -> web.Response:
    """Delete domain from SolarVPS Distributed DNS

    Deletes domain from SolarVPS Distributed DNS

    :param domain: Domain to delete from SolarVPS Distributed DNS
    :type domain: str

    """
    return web.Response(status=200)


async def domains_get(request: web.Request, ) -> web.Response:
    """View all your domains managed by SolarVPS Distributed DNS

    Shows all your domains


    """
    return web.Response(status=200)
