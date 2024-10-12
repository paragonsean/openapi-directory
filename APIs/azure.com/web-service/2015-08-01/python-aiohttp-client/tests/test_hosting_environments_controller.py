# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_response import AddressResponse
from openapi_server.models.csm_usage_quota_collection import CsmUsageQuotaCollection
from openapi_server.models.hosting_environment import HostingEnvironment
from openapi_server.models.hosting_environment_collection import HostingEnvironmentCollection
from openapi_server.models.hosting_environment_diagnostics import HostingEnvironmentDiagnostics
from openapi_server.models.metric_definition import MetricDefinition
from openapi_server.models.metric_definition_collection import MetricDefinitionCollection
from openapi_server.models.resource_metric_collection import ResourceMetricCollection
from openapi_server.models.server_farm_collection import ServerFarmCollection
from openapi_server.models.site_collection import SiteCollection
from openapi_server.models.sku_info_collection import SkuInfoCollection
from openapi_server.models.stamp_capacity_collection import StampCapacityCollection
from openapi_server.models.usage_collection import UsageCollection
from openapi_server.models.worker_pool import WorkerPool
from openapi_server.models.worker_pool_collection import WorkerPoolCollection


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_hosting_environments_create_or_update_hosting_environment(client):
    """Test case for hosting_environments_create_or_update_hosting_environment

    Create or update a hostingEnvironment (App Service Environment).
    """
    hosting_environment_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=hosting_environment_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_hosting_environments_create_or_update_multi_role_pool(client):
    """Test case for hosting_environments_create_or_update_multi_role_pool

    Create or update a multiRole pool.
    """
    multi_role_pool_envelope = {"sku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":0},"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=multi_role_pool_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_hosting_environments_create_or_update_worker_pool(client):
    """Test case for hosting_environments_create_or_update_worker_pool

    Create or update a worker pool.
    """
    worker_pool_envelope = {"sku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":0},"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{worker_pool_name}'.format(resource_group_name='resource_group_name_example', name='name_example', worker_pool_name='worker_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=worker_pool_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_delete_hosting_environment(client):
    """Test case for hosting_environments_delete_hosting_environment

    Delete a hostingEnvironment (App Service Environment).
    """
    params = [('forceDelete', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment(client):
    """Test case for hosting_environments_get_hosting_environment

    Get properties of hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_capacities(client):
    """Test case for hosting_environments_get_hosting_environment_capacities

    Get used, available, and total worker capacity for hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/compute'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_diagnostics(client):
    """Test case for hosting_environments_get_hosting_environment_diagnostics

    Get diagnostic information for hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_diagnostics_item(client):
    """Test case for hosting_environments_get_hosting_environment_diagnostics_item

    Get diagnostic information for hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics/{diagnostics_name}'.format(resource_group_name='resource_group_name_example', name='name_example', diagnostics_name='diagnostics_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_metric_definitions(client):
    """Test case for hosting_environments_get_hosting_environment_metric_definitions

    Get global metric definitions of hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_metrics(client):
    """Test case for hosting_environments_get_hosting_environment_metrics

    Get global metrics of hostingEnvironment (App Service Environment).
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_multi_role_metric_definitions(client):
    """Test case for hosting_environments_get_hosting_environment_multi_role_metric_definitions

    Get metric definitions for a multiRole pool of a hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_multi_role_metrics(client):
    """Test case for hosting_environments_get_hosting_environment_multi_role_metrics

    Get metrics for a multiRole pool of a hostingEnvironment (App Service Environment).
    """
    params = [('startTime', 'start_time_example'),
                    ('endTime', 'end_time_example'),
                    ('timeGrain', 'time_grain_example'),
                    ('details', True),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_multi_role_usages(client):
    """Test case for hosting_environments_get_hosting_environment_multi_role_usages

    Get usages for a multiRole pool of a hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/usages'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_operation(client):
    """Test case for hosting_environments_get_hosting_environment_operation

    Get status of an operation on a hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/operations/{operation_id}'.format(resource_group_name='resource_group_name_example', name='name_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_operations(client):
    """Test case for hosting_environments_get_hosting_environment_operations

    List all currently running operations on the hostingEnvironment (App Service Environment)
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/operations'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_server_farms(client):
    """Test case for hosting_environments_get_hosting_environment_server_farms

    Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/serverfarms'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_sites(client):
    """Test case for hosting_environments_get_hosting_environment_sites

    Get all sites on the hostingEnvironment (App Service Environment).
    """
    params = [('propertiesToInclude', 'properties_to_include_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/sites'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_usages(client):
    """Test case for hosting_environments_get_hosting_environment_usages

    Get global usages of hostingEnvironment (App Service Environment).
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/usages'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_vips(client):
    """Test case for hosting_environments_get_hosting_environment_vips

    Get IP addresses assigned to the hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/virtualip'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_web_hosting_plans(client):
    """Test case for hosting_environments_get_hosting_environment_web_hosting_plans

    Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/webhostingplans'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_web_worker_metric_definitions(client):
    """Test case for hosting_environments_get_hosting_environment_web_worker_metric_definitions

    Get metric definitions for a worker pool of a hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{worker_pool_name}/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', worker_pool_name='worker_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_web_worker_metrics(client):
    """Test case for hosting_environments_get_hosting_environment_web_worker_metrics

    Get metrics for a worker pool of a hostingEnvironment (App Service Environment).
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{worker_pool_name}/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', worker_pool_name='worker_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environment_web_worker_usages(client):
    """Test case for hosting_environments_get_hosting_environment_web_worker_usages

    Get usages for a worker pool of a hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{worker_pool_name}/usages'.format(resource_group_name='resource_group_name_example', name='name_example', worker_pool_name='worker_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_hosting_environments(client):
    """Test case for hosting_environments_get_hosting_environments

    Get all hostingEnvironments (App Service Environments) in a resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_multi_role_pool(client):
    """Test case for hosting_environments_get_multi_role_pool

    Get properties of a multiRole pool.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_multi_role_pool_instance_metric_definitions(client):
    """Test case for hosting_environments_get_multi_role_pool_instance_metric_definitions

    Get metric definitions for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', instance='instance_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_multi_role_pool_instance_metrics(client):
    """Test case for hosting_environments_get_multi_role_pool_instance_metrics

    Get metrics for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).
    """
    params = [('details', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', instance='instance_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_multi_role_pool_skus(client):
    """Test case for hosting_environments_get_multi_role_pool_skus

    Get available skus for scaling a multiRole pool.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/skus'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_multi_role_pools(client):
    """Test case for hosting_environments_get_multi_role_pools

    Get all multi role pools
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_worker_pool(client):
    """Test case for hosting_environments_get_worker_pool

    Get properties of a worker pool.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{worker_pool_name}'.format(resource_group_name='resource_group_name_example', name='name_example', worker_pool_name='worker_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_worker_pool_instance_metric_definitions(client):
    """Test case for hosting_environments_get_worker_pool_instance_metric_definitions

    Get metric definitions for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{worker_pool_name}/instances/{instance}/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', worker_pool_name='worker_pool_name_example', instance='instance_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_worker_pool_instance_metrics(client):
    """Test case for hosting_environments_get_worker_pool_instance_metrics

    Get metrics for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{worker_pool_name}/instances/{instance}/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', worker_pool_name='worker_pool_name_example', instance='instance_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_worker_pool_skus(client):
    """Test case for hosting_environments_get_worker_pool_skus

    Get available skus for scaling a worker pool.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{worker_pool_name}/skus'.format(resource_group_name='resource_group_name_example', name='name_example', worker_pool_name='worker_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_get_worker_pools(client):
    """Test case for hosting_environments_get_worker_pools

    Get all worker pools
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_reboot_hosting_environment(client):
    """Test case for hosting_environments_reboot_hosting_environment

    Reboots all machines in a hostingEnvironment (App Service Environment).
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/reboot'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_resume_hosting_environment(client):
    """Test case for hosting_environments_resume_hosting_environment

    Resumes the hostingEnvironment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/resume'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hosting_environments_suspend_hosting_environment(client):
    """Test case for hosting_environments_suspend_hosting_environment

    Suspends the hostingEnvironment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/suspend'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

