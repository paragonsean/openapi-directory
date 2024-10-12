# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_gateway_definition import ConnectionGatewayDefinition
from openapi_server.models.connection_gateway_definition_collection import ConnectionGatewayDefinitionCollection
from openapi_server.models.connection_gateway_installation_definition import ConnectionGatewayInstallationDefinition
from openapi_server.models.connection_gateway_installation_definition_collection import ConnectionGatewayInstallationDefinitionCollection


pytestmark = pytest.mark.asyncio

async def test_connection_gateway_installations_get(client):
    """Test case for connection_gateway_installations_get

    Gets an installed gateway that the user is an admin of
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/{location}/connectionGatewayInstallations/{gateway_id}'.format(subscription_id='subscription_id_example', location='location_example', gateway_id='gateway_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_gateway_installations_list(client):
    """Test case for connection_gateway_installations_list

    Gets a list of installed gateways that the user is an admin of
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/{location}/connectionGatewayInstallations'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_gateways_create_or_update(client):
    """Test case for connection_gateways_create_or_update

    Replaces a specific gateway
    """
    connection_gateway = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connectionGateways/{connection_gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_gateway_name='connection_gateway_name_example'),
        headers=headers,
        json=connection_gateway,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_gateways_delete(client):
    """Test case for connection_gateways_delete

    Deletes a specific gateway
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connectionGateways/{connection_gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_gateway_name='connection_gateway_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_gateways_get(client):
    """Test case for connection_gateways_get

    Gets a specific gateway
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connectionGateways/{connection_gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_gateway_name='connection_gateway_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_gateways_list(client):
    """Test case for connection_gateways_list

    Lists all of the connection gateways
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/connectionGateways'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_gateways_list_by_resource_group(client):
    """Test case for connection_gateways_list_by_resource_group

    Lists all of the connection gateways
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connectionGateways'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_gateways_update(client):
    """Test case for connection_gateways_update

    Updates a specific gateway
    """
    connection_gateway = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connectionGateways/{connection_gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_gateway_name='connection_gateway_name_example'),
        headers=headers,
        json=connection_gateway,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

