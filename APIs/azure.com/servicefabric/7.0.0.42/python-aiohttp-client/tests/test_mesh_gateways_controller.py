# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.gateway_resource_description import GatewayResourceDescription
from openapi_server.models.paged_gateway_resource_description_list import PagedGatewayResourceDescriptionList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_mesh_gateway_create_or_update(client):
    """Test case for mesh_gateway_create_or_update

    Creates or updates a Gateway resource.
    """
    gateway_resource_description = openapi_server.GatewayResourceDescription()
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/Resources/Gateways/{gateway_resource_name}'.format(gateway_resource_name='gateway_resource_name_example'),
        headers=headers,
        json=gateway_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_gateway_delete(client):
    """Test case for mesh_gateway_delete

    Deletes the Gateway resource.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/Resources/Gateways/{gateway_resource_name}'.format(gateway_resource_name='gateway_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_gateway_get(client):
    """Test case for mesh_gateway_get

    Gets the Gateway resource with the given name.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Gateways/{gateway_resource_name}'.format(gateway_resource_name='gateway_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_gateway_list(client):
    """Test case for mesh_gateway_list

    Lists all the gateway resources.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Gateways',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

