from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain_domainname_get200_response import DomainDomainnameGet200Response
from openapi_server import util


async def domain_domainname_get(request: web.Request, domainname) -> web.Response:
    """Get a Domain

    This endpoint allows you to get the data of a given PhantAuth domain. To use the PhantAuth services, you don&#39;t need this endpoint. It is, therefore, mainly used for debug/diagnostic purposes in tenant customization.  Domainname is the fully qualified DNS name of the domain you get (e.g. *phantauth.net* or *phantauth.cf*).

    :param domainname: The domain ID integrated in the &#x60;sub&#x60; property.
    :type domainname: str

    """
    return web.Response(status=200)
