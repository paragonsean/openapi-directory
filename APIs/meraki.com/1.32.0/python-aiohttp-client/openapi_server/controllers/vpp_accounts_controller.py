from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_sm_vpp_accounts200_response_inner import GetOrganizationSmVppAccounts200ResponseInner
from openapi_server import util


async def get_organization_sm_vpp_account_1(request: web.Request, organization_id, vpp_account_id) -> web.Response:
    """Get a hash containing the unparsed token of the VPP account with the given ID

    Get a hash containing the unparsed token of the VPP account with the given ID

    :param organization_id: 
    :type organization_id: str
    :param vpp_account_id: 
    :type vpp_account_id: str

    """
    return web.Response(status=200)


async def get_organization_sm_vpp_accounts_1(request: web.Request, organization_id) -> web.Response:
    """List the VPP accounts in the organization

    List the VPP accounts in the organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)
