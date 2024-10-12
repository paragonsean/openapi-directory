# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_appliance_vpn_third_party_vpn_peers200_response import GetOrganizationApplianceVpnThirdPartyVPNPeers200Response
from openapi_server.models.update_organization_appliance_vpn_third_party_vpn_peers_request import UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest


pytestmark = pytest.mark.asyncio

async def test_get_organization_appliance_vpn_third_party_vpn_peers_2(client):
    """Test case for get_organization_appliance_vpn_third_party_vpn_peers_2

    Return the third party VPN peers for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/appliance/vpn/thirdPartyVPNPeers'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_appliance_vpn_third_party_vpn_peers_2(client):
    """Test case for update_organization_appliance_vpn_third_party_vpn_peers_2

    Update the third party VPN peers for an organization
    """
    body = openapi_server.UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/appliance/vpn/thirdPartyVPNPeers'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

