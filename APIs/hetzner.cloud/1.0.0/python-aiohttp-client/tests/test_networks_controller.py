# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_request import CreateNetworkRequest
from openapi_server.models.networks_get200_response import NetworksGet200Response
from openapi_server.models.networks_post201_response import NetworksPost201Response
from openapi_server.models.update_network_request import UpdateNetworkRequest


pytestmark = pytest.mark.asyncio

async def test_networks_get(client):
    """Test case for networks_get

    Get all Networks
    """
    params = [('name', 'name_example'),
                    ('label_selector', 'label_selector_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/networks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_delete(client):
    """Test case for networks_id_delete

    Delete a Network
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/networks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_get(client):
    """Test case for networks_id_get

    Get a Network
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/networks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_id_put(client):
    """Test case for networks_id_put

    Update a Network
    """
    body = {"name":"new-name","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/networks/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networks_post(client):
    """Test case for networks_post

    Create a Network
    """
    body = {"ip_range":"10.0.0.0/16","routes":[{"destination":"10.100.1.0/24","gateway":"10.0.1.1"},{"destination":"10.100.1.0/24","gateway":"10.0.1.1"}],"name":"mynet","subnets":[{"ip_range":"10.0.1.0/24","network_zone":"eu-central","vswitch_id":1000,"type":"cloud"},{"ip_range":"10.0.1.0/24","network_zone":"eu-central","vswitch_id":1000,"type":"cloud"}],"labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/networks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

