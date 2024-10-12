# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_sm_target_group_request import CreateNetworkSmTargetGroupRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_sm_target_group_1(client):
    """Test case for create_network_sm_target_group_1

    Add a target group
    """
    body = openapi_server.CreateNetworkSmTargetGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/targetGroups'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_sm_target_group_1(client):
    """Test case for delete_network_sm_target_group_1

    Delete a target group from a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/sm/targetGroups/{target_group_id}'.format(network_id='network_id_example', target_group_id='target_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_target_group_1(client):
    """Test case for get_network_sm_target_group_1

    Return a target group
    """
    params = [('withDetails', True)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/targetGroups/{target_group_id}'.format(network_id='network_id_example', target_group_id='target_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_target_groups_1(client):
    """Test case for get_network_sm_target_groups_1

    List the target groups in this network
    """
    params = [('withDetails', True)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/targetGroups'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_sm_target_group_1(client):
    """Test case for update_network_sm_target_group_1

    Update a target group
    """
    body = openapi_server.CreateNetworkSmTargetGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/sm/targetGroups/{target_group_id}'.format(network_id='network_id_example', target_group_id='target_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

