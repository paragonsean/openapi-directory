# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.network_resource_description import NetworkResourceDescription
from openapi_server.models.paged_network_resource_description_list import PagedNetworkResourceDescriptionList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_mesh_network_create_or_update(client):
    """Test case for mesh_network_create_or_update

    Creates or updates a Network resource.
    """
    network_resource_description = openapi_server.NetworkResourceDescription()
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/Resources/Networks/{network_resource_name}'.format(network_resource_name='network_resource_name_example'),
        headers=headers,
        json=network_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_network_delete(client):
    """Test case for mesh_network_delete

    Deletes the Network resource.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/Resources/Networks/{network_resource_name}'.format(network_resource_name='network_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_network_get(client):
    """Test case for mesh_network_get

    Gets the Network resource with the given name.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Networks/{network_resource_name}'.format(network_resource_name='network_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_network_list(client):
    """Test case for mesh_network_list

    Lists all the network resources.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Networks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

