# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_service_plan_patch_resource import AppServicePlanPatchResource
from openapi_server.models.app_service_plans_create_or_update_vnet_route_request import AppServicePlansCreateOrUpdateVnetRouteRequest
from openapi_server.models.app_service_plans_get200_response import AppServicePlansGet200Response
from openapi_server.models.app_service_plans_get_hybrid_connection200_response import AppServicePlansGetHybridConnection200Response
from openapi_server.models.app_service_plans_get_vnet_from_server_farm200_response import AppServicePlansGetVnetFromServerFarm200Response
from openapi_server.models.app_service_plans_get_vnet_gateway200_response import AppServicePlansGetVnetGateway200Response
from openapi_server.models.app_service_plans_list200_response import AppServicePlansList200Response
from openapi_server.models.app_service_plans_list200_response_value_inner_sku_capabilities_inner import AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner
from openapi_server.models.app_service_plans_list_hybrid_connection_keys200_response import AppServicePlansListHybridConnectionKeys200Response
from openapi_server.models.app_service_plans_list_metric_defintions200_response import AppServicePlansListMetricDefintions200Response
from openapi_server.models.app_service_plans_list_metrics200_response import AppServicePlansListMetrics200Response
from openapi_server.models.app_service_plans_list_usages200_response import AppServicePlansListUsages200Response
from openapi_server.models.app_service_plans_list_vnets200_response_inner import AppServicePlansListVnets200ResponseInner
from openapi_server.models.app_service_plans_list_vnets200_response_inner_properties_routes_inner import AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner
from openapi_server.models.app_service_plans_list_web_apps200_response import AppServicePlansListWebApps200Response
from openapi_server.models.hybrid_connection_collection import HybridConnectionCollection
from openapi_server.models.hybrid_connection_limits import HybridConnectionLimits
from openapi_server.models.resource_collection import ResourceCollection


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_create_or_update(client):
    """Test case for app_service_plans_create_or_update

    Creates or updates an App Service Plan.
    """
    app_service_plan = openapi_server.AppServicePlansGet200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=app_service_plan,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_create_or_update_vnet_route(client):
    """Test case for app_service_plans_create_or_update_vnet_route

    Create or update a Virtual Network route in an App Service plan.
    """
    route = openapi_server.AppServicePlansCreateOrUpdateVnetRouteRequest()
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

async def test_app_service_plans_delete(client):
    """Test case for app_service_plans_delete

    Delete an App Service plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
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

async def test_app_service_plans_delete_hybrid_connection(client):
    """Test case for app_service_plans_delete_hybrid_connection

    Delete a Hybrid Connection in use in an App Service plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_delete_vnet_route(client):
    """Test case for app_service_plans_delete_vnet_route

    Delete a Virtual Network route in an App Service plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
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

async def test_app_service_plans_get(client):
    """Test case for app_service_plans_get

    Get an App Service plan.
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

async def test_app_service_plans_get_hybrid_connection(client):
    """Test case for app_service_plans_get_hybrid_connection

    Retrieve a Hybrid Connection in use in an App Service plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_get_hybrid_connection_plan_limit(client):
    """Test case for app_service_plans_get_hybrid_connection_plan_limit

    Get the maximum number of Hybrid Connections allowed in an App Service plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionPlanLimits/limit'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_get_route_for_vnet(client):
    """Test case for app_service_plans_get_route_for_vnet

    Get a Virtual Network route in an App Service plan.
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

async def test_app_service_plans_get_server_farm_skus(client):
    """Test case for app_service_plans_get_server_farm_skus

    Gets all selectable SKUs for a given App Service Plan
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/skus'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_get_vnet_from_server_farm(client):
    """Test case for app_service_plans_get_vnet_from_server_farm

    Get a Virtual Network associated with an App Service plan.
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

async def test_app_service_plans_get_vnet_gateway(client):
    """Test case for app_service_plans_get_vnet_gateway

    Get a Virtual Network gateway.
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

async def test_app_service_plans_list(client):
    """Test case for app_service_plans_list

    Get all App Service plans for a subscription.
    """
    params = [('detailed', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/serverfarms'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_list_by_resource_group(client):
    """Test case for app_service_plans_list_by_resource_group

    Get all App Service plans in a resource group.
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

async def test_app_service_plans_list_capabilities(client):
    """Test case for app_service_plans_list_capabilities

    List all capabilities of an App Service plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/capabilities'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_list_hybrid_connection_keys(client):
    """Test case for app_service_plans_list_hybrid_connection_keys

    Get the send key name and value of a Hybrid Connection.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}/listKeys'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_list_hybrid_connections(client):
    """Test case for app_service_plans_list_hybrid_connections

    Retrieve all Hybrid Connections in use in an App Service plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionRelays'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_list_metric_defintions(client):
    """Test case for app_service_plans_list_metric_defintions

    Get metrics that can be queried for an App Service plan, and their definitions.
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

async def test_app_service_plans_list_metrics(client):
    """Test case for app_service_plans_list_metrics

    Get metrics for an App Service plan.
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

async def test_app_service_plans_list_routes_for_vnet(client):
    """Test case for app_service_plans_list_routes_for_vnet

    Get all routes that are associated with a Virtual Network in an App Service plan.
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

async def test_app_service_plans_list_usages(client):
    """Test case for app_service_plans_list_usages

    Gets server farm usage information
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/usages'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_list_vnets(client):
    """Test case for app_service_plans_list_vnets

    Get all Virtual Networks associated with an App Service plan.
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

async def test_app_service_plans_list_web_apps(client):
    """Test case for app_service_plans_list_web_apps

    Get all apps associated with an App Service plan.
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

async def test_app_service_plans_list_web_apps_by_hybrid_connection(client):
    """Test case for app_service_plans_list_web_apps_by_hybrid_connection

    Get all apps that use a Hybrid Connection in an App Service Plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespace_name}/relays/{relay_name}/sites'.format(resource_group_name='resource_group_name_example', name='name_example', namespace_name='namespace_name_example', relay_name='relay_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_reboot_worker(client):
    """Test case for app_service_plans_reboot_worker

    Reboot a worker machine in an App Service plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
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

async def test_app_service_plans_restart_web_apps(client):
    """Test case for app_service_plans_restart_web_apps

    Restart all apps in an App Service plan.
    """
    params = [('softRestart', True),
                    ('api-version', 'api_version_example')]
    headers = { 
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

async def test_app_service_plans_update(client):
    """Test case for app_service_plans_update

    Creates or updates an App Service Plan.
    """
    app_service_plan = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/serverfarms/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=app_service_plan,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_plans_update_vnet_gateway(client):
    """Test case for app_service_plans_update_vnet_gateway

    Update a Virtual Network gateway.
    """
    connection_envelope = openapi_server.AppServicePlansGetVnetGateway200Response()
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

async def test_app_service_plans_update_vnet_route(client):
    """Test case for app_service_plans_update_vnet_route

    Create or update a Virtual Network route in an App Service plan.
    """
    route = openapi_server.AppServicePlansCreateOrUpdateVnetRouteRequest()
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

