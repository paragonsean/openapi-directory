# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_appliance_prefixes_delegated_static_request import CreateNetworkAppliancePrefixesDelegatedStaticRequest
from openapi_server.models.get_network_appliance_prefixes_delegated_statics200_response_inner import GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner
from openapi_server.models.update_network_appliance_prefixes_delegated_static_request import UpdateNetworkAppliancePrefixesDelegatedStaticRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_appliance_prefixes_delegated_static_2(client):
    """Test case for create_network_appliance_prefixes_delegated_static_2

    Add a static delegated prefix from a network
    """
    body = openapi_server.CreateNetworkAppliancePrefixesDelegatedStaticRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/appliance/prefixes/delegated/statics'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_appliance_prefixes_delegated_static_2(client):
    """Test case for delete_network_appliance_prefixes_delegated_static_2

    Delete a static delegated prefix from a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/appliance/prefixes/delegated/statics/{static_delegated_prefix_id}'.format(network_id='network_id_example', static_delegated_prefix_id='static_delegated_prefix_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_appliance_prefixes_delegated_2(client):
    """Test case for get_device_appliance_prefixes_delegated_2

    Return current delegated IPv6 prefixes on an appliance.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/appliance/prefixes/delegated'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_appliance_prefixes_delegated_vlan_assignments_2(client):
    """Test case for get_device_appliance_prefixes_delegated_vlan_assignments_2

    Return prefixes assigned to all IPv6 enabled VLANs on an appliance.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/appliance/prefixes/delegated/vlanAssignments'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_prefixes_delegated_static_2(client):
    """Test case for get_network_appliance_prefixes_delegated_static_2

    Return a static delegated prefix from a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/prefixes/delegated/statics/{static_delegated_prefix_id}'.format(network_id='network_id_example', static_delegated_prefix_id='static_delegated_prefix_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_prefixes_delegated_statics_2(client):
    """Test case for get_network_appliance_prefixes_delegated_statics_2

    List static delegated prefixes for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/prefixes/delegated/statics'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_prefixes_delegated_static_2(client):
    """Test case for update_network_appliance_prefixes_delegated_static_2

    Update a static delegated prefix from a network
    """
    body = openapi_server.UpdateNetworkAppliancePrefixesDelegatedStaticRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/prefixes/delegated/statics/{static_delegated_prefix_id}'.format(network_id='network_id_example', static_delegated_prefix_id='static_delegated_prefix_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

