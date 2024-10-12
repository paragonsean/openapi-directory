# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.claim_into_organization_request import ClaimIntoOrganizationRequest
from openapi_server.models.clone_organization_request import CloneOrganizationRequest
from openapi_server.models.update_organization_third_party_vpn_peers_request import UpdateOrganizationThirdPartyVPNPeersRequest


pytestmark = pytest.mark.asyncio

async def test_claim_into_organization(client):
    """Test case for claim_into_organization

    Claim a list of devices, licenses, and/or orders into an organization
    """
    body = openapi_server.ClaimIntoOrganizationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/organizations/{organization_id}/claim'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clone_organization(client):
    """Test case for clone_organization

    Create a new organization by cloning the addressed organization
    """
    body = openapi_server.CloneOrganizationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/organizations/{organization_id}/clone'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization(client):
    """Test case for get_organization

    Return an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_device_statuses(client):
    """Test case for get_organization_device_statuses

    List the status of every Meraki device in the organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/deviceStatuses'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory(client):
    """Test case for get_organization_inventory

    Return the inventory for an organization
    """
    params = [('includeLicenseInfo', True)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/inventory'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_third_party_vpn_peers(client):
    """Test case for get_organization_third_party_vpn_peers

    Return the third party VPN peers for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/thirdPartyVPNPeers'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_uplinks_loss_and_latency(client):
    """Test case for get_organization_uplinks_loss_and_latency

    Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('uplink', 'uplink_example'),
                    ('ip', 'ip_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/uplinksLossAndLatency'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations(client):
    """Test case for get_organizations

    List the organizations that the user has privileges on
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_third_party_vpn_peers(client):
    """Test case for update_organization_third_party_vpn_peers

    Update the third party VPN peers for an organization
    """
    body = openapi_server.UpdateOrganizationThirdPartyVPNPeersRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/organizations/{organization_id}/thirdPartyVPNPeers'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

