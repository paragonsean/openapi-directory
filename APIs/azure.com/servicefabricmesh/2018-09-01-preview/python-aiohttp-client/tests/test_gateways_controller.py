# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.gateway_resource_description import GatewayResourceDescription
from openapi_server.models.gateway_resource_description_list import GatewayResourceDescriptionList


pytestmark = pytest.mark.asyncio

async def test_gateway_create(client):
    """Test case for gateway_create

    Creates or updates a gateway resource.
    """
    gateway_resource_description = {"properties":{"tcp":[{"port":6,"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"name":"name"},{"port":6,"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"name":"name"}],"sourceNetwork":{"name":"name","endpointRefs":[{"name":"name"},{"name":"name"}]},"ipAddress":"ipAddress","description":"description","http":[{"port":0,"hosts":[{"routes":[{"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"match":{"headers":[{"name":"name","type":"exact","value":"value"},{"name":"name","type":"exact","value":"value"}],"path":{"type":"prefix","value":"value","rewrite":"rewrite"}},"name":"name"},{"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"match":{"headers":[{"name":"name","type":"exact","value":"value"},{"name":"name","type":"exact","value":"value"}],"path":{"type":"prefix","value":"value","rewrite":"rewrite"}},"name":"name"}],"name":"name"},{"routes":[{"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"match":{"headers":[{"name":"name","type":"exact","value":"value"},{"name":"name","type":"exact","value":"value"}],"path":{"type":"prefix","value":"value","rewrite":"rewrite"}},"name":"name"},{"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"match":{"headers":[{"name":"name","type":"exact","value":"value"},{"name":"name","type":"exact","value":"value"}],"path":{"type":"prefix","value":"value","rewrite":"rewrite"}},"name":"name"}],"name":"name"}],"name":"name"},{"port":0,"hosts":[{"routes":[{"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"match":{"headers":[{"name":"name","type":"exact","value":"value"},{"name":"name","type":"exact","value":"value"}],"path":{"type":"prefix","value":"value","rewrite":"rewrite"}},"name":"name"},{"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"match":{"headers":[{"name":"name","type":"exact","value":"value"},{"name":"name","type":"exact","value":"value"}],"path":{"type":"prefix","value":"value","rewrite":"rewrite"}},"name":"name"}],"name":"name"},{"routes":[{"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"match":{"headers":[{"name":"name","type":"exact","value":"value"},{"name":"name","type":"exact","value":"value"}],"path":{"type":"prefix","value":"value","rewrite":"rewrite"}},"name":"name"},{"destination":{"endpointName":"endpointName","serviceName":"serviceName","applicationName":"applicationName"},"match":{"headers":[{"name":"name","type":"exact","value":"value"},{"name":"name","type":"exact","value":"value"}],"path":{"type":"prefix","value":"value","rewrite":"rewrite"}},"name":"name"}],"name":"name"}],"name":"name"}],"statusDetails":"statusDetails","provisioningState":"provisioningState","destinationNetwork":{"name":"name","endpointRefs":[{"name":"name"},{"name":"name"}]},"status":"Unknown"}}
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/gateways/{gateway_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_resource_name='gateway_resource_name_example'),
        headers=headers,
        json=gateway_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gateway_delete(client):
    """Test case for gateway_delete

    Deletes the gateway resource.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/gateways/{gateway_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_resource_name='gateway_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gateway_get(client):
    """Test case for gateway_get

    Gets the gateway resource with the given name.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/gateways/{gateway_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_resource_name='gateway_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gateway_list_by_resource_group(client):
    """Test case for gateway_list_by_resource_group

    Gets all the gateway resources in a given resource group.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/gateways'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gateway_list_by_subscription(client):
    """Test case for gateway_list_by_subscription

    Gets all the gateway resources in a given subscription.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceFabricMesh/gateways'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

