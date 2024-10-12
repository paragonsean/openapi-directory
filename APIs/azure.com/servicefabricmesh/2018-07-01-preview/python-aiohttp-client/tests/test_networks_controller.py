# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.network_resource_description import NetworkResourceDescription
from openapi_server.models.network_resource_description_list import NetworkResourceDescriptionList


pytestmark = pytest.mark.asyncio

async def test_network_create(client):
    """Test case for network_create

    Creates or updates a network resource.
    """
    network_resource_description = {"properties":{"ingressConfig":{"layer4":[{"name":"name","publicPort":0,"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},{"name":"name","publicPort":0,"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"}],"qosLevel":"Bronze","publicIPAddress":"publicIPAddress"},"addressPrefix":"addressPrefix","description":"description","provisioningState":"provisioningState"}}
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/networks/{network_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', network_name='network_name_example'),
        headers=headers,
        json=network_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_delete(client):
    """Test case for network_delete

    Deletes the network resource.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/networks/{network_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', network_name='network_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_get(client):
    """Test case for network_get

    Gets the network resource.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/networks/{network_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', network_name='network_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_list_by_resource_group(client):
    """Test case for network_list_by_resource_group

    Gets all the network resources in a given resource group.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/networks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_list_by_subscription(client):
    """Test case for network_list_by_subscription

    Gets all the network resources in a given subscription.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceFabricMesh/networks'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

