# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.metric_definition_collection import MetricDefinitionCollection
from openapi_server.models.resource_metric_collection import ResourceMetricCollection
from openapi_server.models.server_farm_collection import ServerFarmCollection
from openapi_server.models.server_farm_with_rich_sku import ServerFarmWithRichSku
from openapi_server.models.site_collection import SiteCollection
from openapi_server.models.vnet_gateway import VnetGateway
from openapi_server.models.vnet_info import VnetInfo
from openapi_server.models.vnet_route import VnetRoute


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_server_farms_create_or_update_server_farm(client):
    """Test case for server_farms_create_or_update_server_farm

    Creates or updates an App Service Plan
    """
    server_farm_envelope = {"sku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":0},"properties":"{}"}
    params = [('allowPendingState', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=server_farm_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_server_farms_create_or_update_vnet_route(client):
    """Test case for server_farms_create_or_update_vnet_route

    Creates a new route or updates an existing route for a vnet in an app service plan.
    """
    route = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnet_name}/routes/{route_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', route_name='route_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=route,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_delete_server_farm(client):
    """Test case for server_farms_delete_server_farm

    Deletes a App Service Plan
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_delete_vnet_route(client):
    """Test case for server_farms_delete_vnet_route

    Deletes an existing route for a vnet in an app service plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnet_name}/routes/{route_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', route_name='route_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_route_for_vnet(client):
    """Test case for server_farms_get_route_for_vnet

    Gets a specific route associated with a vnet, in an app service plan
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnet_name}/routes/{route_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', route_name='route_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_routes_for_vnet(client):
    """Test case for server_farms_get_routes_for_vnet

    Gets a list of all routes associated with a vnet, in an app service plan
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnet_name}/routes'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_server_farm(client):
    """Test case for server_farms_get_server_farm

    Gets specified App Service Plan in a resource group
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_server_farm_metric_defintions(client):
    """Test case for server_farms_get_server_farm_metric_defintions

    List of metrics that can be queried for an App Service Plan
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_server_farm_metrics(client):
    """Test case for server_farms_get_server_farm_metrics

    Queries for App Service Plan metrics
    """
    params = [('details', True),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_server_farm_operation(client):
    """Test case for server_farms_get_server_farm_operation

    Gets a server farm operation
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/operationresults/{operation_id}'.format(resource_group_name='resource_group_name_example', name='name_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_server_farm_sites(client):
    """Test case for server_farms_get_server_farm_sites

    Gets list of Apps associated with an App Service Plan
    """
    params = [('$skipToken', 'skip_token_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 'top_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/sites'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_server_farm_vnet_gateway(client):
    """Test case for server_farms_get_server_farm_vnet_gateway

    Gets the vnet gateway.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_server_farms(client):
    """Test case for server_farms_get_server_farms

    Gets collection of App Service Plans in a resource group for a given subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_vnet_from_server_farm(client):
    """Test case for server_farms_get_vnet_from_server_farm

    Gets a vnet associated with an App Service Plan
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_get_vnets_for_server_farm(client):
    """Test case for server_farms_get_vnets_for_server_farm

    Gets list of VNets associated with App Service Plan
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_reboot_worker_for_server_farm(client):
    """Test case for server_farms_reboot_worker_for_server_farm

    Submit a reboot request for a worker machine in the specified server farm
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/workers/{worker_name}/reboot'.format(resource_group_name='resource_group_name_example', name='name_example', worker_name='worker_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_farms_restart_sites_for_server_farm(client):
    """Test case for server_farms_restart_sites_for_server_farm

    Restarts web apps in a specified App Service Plan
    """
    params = [('softRestart', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/restartSites'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_server_farms_update_server_farm_vnet_gateway(client):
    """Test case for server_farms_update_server_farm_vnet_gateway

    Updates the vnet gateway
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_server_farms_update_vnet_route(client):
    """Test case for server_farms_update_vnet_route

    Creates a new route or updates an existing route for a vnet in an app service plan.
    """
    route = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnet_name}/routes/{route_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', route_name='route_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=route,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

