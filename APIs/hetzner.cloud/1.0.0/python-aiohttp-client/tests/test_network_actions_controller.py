# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.add_delete_route_request import AddDeleteRouteRequest
from openapi_server.models.add_subnet_request import AddSubnetRequest
from openapi_server.models.change_ip_range_request import ChangeIPRangeRequest
from openapi_server.models.change_protection_request1 import ChangeProtectionRequest1
from openapi_server.models.delete_subnet_request import DeleteSubnetRequest


pytestmark = pytest.mark.asyncio

async def test_networks_id_actions_action_id_get(client):
    """Test case for networks_id_actions_action_id_get

    Get an Action for a Network
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/networks/{id}/actions/{action_id}'.format(id=56, action_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_actions_add_route_post(client):
    """Test case for networks_id_actions_add_route_post

    Add a route to a Network
    """
    body = {"destination":"10.100.1.0/24","gateway":"10.0.1.1"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/networks/{id}/actions/add_route'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_actions_add_subnet_post(client):
    """Test case for networks_id_actions_add_subnet_post

    Add a subnet to a Network
    """
    body = {"ip_range":"10.0.1.0/24","network_zone":"eu-central","vswitch_id":1000,"type":"cloud"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/networks/{id}/actions/add_subnet'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_actions_change_ip_range_post(client):
    """Test case for networks_id_actions_change_ip_range_post

    Change IP range of a Network
    """
    body = {"ip_range":"10.0.0.0/12"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/networks/{id}/actions/change_ip_range'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_actions_change_protection_post(client):
    """Test case for networks_id_actions_change_protection_post

    Change Network Protection
    """
    body = openapi_server.ChangeProtectionRequest1()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/networks/{id}/actions/change_protection'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_actions_delete_route_post(client):
    """Test case for networks_id_actions_delete_route_post

    Delete a route from a Network
    """
    body = {"destination":"10.100.1.0/24","gateway":"10.0.1.1"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/networks/{id}/actions/delete_route'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_actions_delete_subnet_post(client):
    """Test case for networks_id_actions_delete_subnet_post

    Delete a subnet from a Network
    """
    body = {"ip_range":"10.0.1.0/24"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/networks/{id}/actions/delete_subnet'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_actions_get(client):
    """Test case for networks_id_actions_get

    Get all Actions for a Network
    """
    params = [('sort', 'sort_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/networks/{id}/actions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

