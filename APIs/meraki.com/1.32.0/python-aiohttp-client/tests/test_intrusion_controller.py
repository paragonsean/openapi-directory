# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_appliance_security_intrusion_request import UpdateNetworkApplianceSecurityIntrusionRequest
from openapi_server.models.update_organization_appliance_security_intrusion_request import UpdateOrganizationApplianceSecurityIntrusionRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_security_intrusion_2(client):
    """Test case for get_network_appliance_security_intrusion_2

    Returns all supported intrusion settings for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/security/intrusion'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_appliance_security_intrusion_2(client):
    """Test case for get_organization_appliance_security_intrusion_2

    Returns all supported intrusion settings for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/appliance/security/intrusion'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_security_intrusion_2(client):
    """Test case for update_network_appliance_security_intrusion_2

    Set the supported intrusion settings for an MX network
    """
    body = openapi_server.UpdateNetworkApplianceSecurityIntrusionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/security/intrusion'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_appliance_security_intrusion_2(client):
    """Test case for update_organization_appliance_security_intrusion_2

    Sets supported intrusion settings for an organization
    """
    body = openapi_server.UpdateOrganizationApplianceSecurityIntrusionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/appliance/security/intrusion'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

