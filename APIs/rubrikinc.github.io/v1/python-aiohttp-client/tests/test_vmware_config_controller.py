# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.preferred_cdp_network_protocol import PreferredCdpNetworkProtocol
from openapi_server.models.preferred_cdp_network_protocol_object import PreferredCdpNetworkProtocolObject
from openapi_server.models.vmware_network_collection import VmwareNetworkCollection


pytestmark = pytest.mark.asyncio

async def test_get_preferred_cdp_network_protocol(client):
    """Test case for get_preferred_cdp_network_protocol

    Returns the current preference of CDM between IPv4 and IPv6 for CDP data transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/config/cdp/get_preferred_cdp_network_protocol',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmware_recovery_networks(client):
    """Test case for get_vmware_recovery_networks

    Get all the VMware recovery networks for a compute resource ID
    """
    params = [('compute_resource_id', 'compute_resource_id_example'),
                    ('compute_resource_type', 'compute_resource_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/config/recovery/networks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_preferred_cdp_network_protocol(client):
    """Test case for set_preferred_cdp_network_protocol

    Set the current preference of CDM between IPv4 and IPv6 for CDP data transfer
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/vmware/config/cdp/set_preferred_cdp_network_protocol',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

