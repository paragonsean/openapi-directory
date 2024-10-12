from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_sm_apns_cert200_response import GetOrganizationSmApnsCert200Response
from openapi_server import util


async def get_organization_sm_apns_cert_1(request: web.Request, organization_id) -> web.Response:
    """Get the organization&#39;s APNS certificate

    Get the organization&#39;s APNS certificate

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)
