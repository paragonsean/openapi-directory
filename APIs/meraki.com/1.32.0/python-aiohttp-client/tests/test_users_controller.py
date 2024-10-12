# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_sm_device_device_profiles200_response_inner import GetNetworkSmDeviceDeviceProfiles200ResponseInner
from openapi_server.models.get_network_sm_device_softwares200_response_inner import GetNetworkSmDeviceSoftwares200ResponseInner
from openapi_server.models.get_network_sm_users200_response_inner import GetNetworkSmUsers200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_delete_organization_user_1(client):
    """Test case for delete_organization_user_1

    Delete a user and all of its authentication methods.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/users/{user_id}'.format(organization_id='organization_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_user_device_profiles_1(client):
    """Test case for get_network_sm_user_device_profiles_1

    Get the profiles associated with a user
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/users/{user_id}/deviceProfiles'.format(network_id='network_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_user_softwares_1(client):
    """Test case for get_network_sm_user_softwares_1

    Get a list of softwares associated with a user
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/users/{user_id}/softwares'.format(network_id='network_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_users_1(client):
    """Test case for get_network_sm_users_1

    List the owners in an SM network with various specified fields and filters
    """
    params = [('ids', ['ids_example']),
                    ('usernames', ['usernames_example']),
                    ('emails', ['emails_example']),
                    ('scope', ['scope_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/users'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

