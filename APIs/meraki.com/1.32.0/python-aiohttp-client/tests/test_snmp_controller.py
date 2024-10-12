# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_snmp_request import UpdateNetworkSnmpRequest
from openapi_server.models.update_organization_snmp_request import UpdateOrganizationSnmpRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_snmp_1(client):
    """Test case for get_network_snmp_1

    Return the SNMP settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/snmp'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_snmp_1(client):
    """Test case for get_organization_snmp_1

    Return the SNMP settings for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/snmp'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_snmp_1(client):
    """Test case for update_network_snmp_1

    Update the SNMP settings for a network
    """
    body = openapi_server.UpdateNetworkSnmpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/snmp'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_snmp_1(client):
    """Test case for update_organization_snmp_1

    Update the SNMP settings for an organization
    """
    body = openapi_server.UpdateOrganizationSnmpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/snmp'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

