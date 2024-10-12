from typing import List, Dict
from aiohttp import web

from openapi_server.models.tenant_tenantname_get200_response import TenantTenantnameGet200Response
from openapi_server import util


async def tenant_tenantname_get(request: web.Request, tenantname) -> web.Response:
    """Get a Tenant

    This endpoint allows you to get the data of a given PhantAuth tenant. To use the PhantAuth services, you don&#39;t need this endpoint. It is, therefore, mainly used for debug/diagnostic purposes in tenant customization.  Tenantname is the name of the full DNS domain of the tenant you get. In the case of an official and shared tenant (phantauth.net and phantauth.cf DNS domains), the DNS domain can be omitted (e.g. *default* or *faker*).

    :param tenantname: The tenant ID integrated in the &#x60;sub&#x60; property.
    :type tenantname: str

    """
    return web.Response(status=200)
