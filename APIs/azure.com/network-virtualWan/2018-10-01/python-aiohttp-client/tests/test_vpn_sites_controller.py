# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.p2s_vpn_gateways_list_default_response import P2sVpnGatewaysListDefaultResponse
from openapi_server.models.p2s_vpn_gateways_update_tags_request import P2sVpnGatewaysUpdateTagsRequest
from openapi_server.models.vpn_site import VpnSite


pytestmark = pytest.mark.asyncio

async def test_vpn_sites_update_tags(client):
    """Test case for vpn_sites_update_tags

    
    """
    vpn_site_parameters = openapi_server.P2sVpnGatewaysUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnSites/{vpn_site_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vpn_site_name='vpn_site_name_example'),
        headers=headers,
        json=vpn_site_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

