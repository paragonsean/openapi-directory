from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_an_organizations_entitlement_value(request: web.Request, org_id, entitlement_key) -> web.Response:
    """Get an organization&#39;s entitlement value

    

    :param org_id: The organization ID to query the entitlement for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param entitlement_key: The entitlement to query.
    :type entitlement_key: str

    """
    return web.Response(status=200)


async def list_all_entitlements(request: web.Request, org_id) -> web.Response:
    """List all entitlements

    

    :param org_id: The organization ID to list entitlements for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str

    """
    return web.Response(status=200)
