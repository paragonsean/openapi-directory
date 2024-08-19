# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_response import AddressResponse
from openapi_server.models.app_service_environment_collection import AppServiceEnvironmentCollection
from openapi_server.models.app_service_environment_patch_resource import AppServiceEnvironmentPatchResource
from openapi_server.models.app_service_environment_resource import AppServiceEnvironmentResource
from openapi_server.models.app_service_environments_list_app_service_plans200_response import AppServiceEnvironmentsListAppServicePlans200Response
from openapi_server.models.app_service_environments_list_metrics200_response import AppServiceEnvironmentsListMetrics200Response
from openapi_server.models.app_service_environments_list_multi_role_pool_instance_metric_definitions200_response import AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response
from openapi_server.models.app_service_environments_list_operations200_response_inner import AppServiceEnvironmentsListOperations200ResponseInner
from openapi_server.models.app_service_environments_list_usages200_response import AppServiceEnvironmentsListUsages200Response
from openapi_server.models.app_service_environments_resume200_response import AppServiceEnvironmentsResume200Response
from openapi_server.models.hosting_environment_diagnostics import HostingEnvironmentDiagnostics
from openapi_server.models.metric_definition import MetricDefinition
from openapi_server.models.sku_info_collection import SkuInfoCollection
from openapi_server.models.stamp_capacity_collection import StampCapacityCollection
from openapi_server.models.usage_collection import UsageCollection
from openapi_server.models.worker_pool_collection import WorkerPoolCollection
from openapi_server.models.worker_pool_resource import WorkerPoolResource


pytestmark = pytest.mark.asyncio

async def test_app_service_environments_create_or_update(client):
    """Test case for app_service_environments_create_or_update

    Create or update an App Service Environment.
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

async def test_app_service_environments_create_or_update_multi_role_pool(client):
    """Test case for app_service_environments_create_or_update_multi_role_pool

    Create or update a multi-role pool.
    """
    multi_role_pool_envelope = {"sku":"{}","properties":"{}"}
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

async def test_app_service_environments_create_or_update_worker_pool(client):
    """Test case for app_service_environments_create_or_update_worker_pool

    Create or update a worker pool.
    """
    worker_pool_envelope = {"sku":"{}","properties":"{}"}
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

async def test_app_service_environments_delete(client):
    """Test case for app_service_environments_delete

    Delete an App Service Environment.
    """
    params = [('forceDelete', True),
                    ('api-version', 'api_version_example')]
    headers = { 
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

async def test_app_service_environments_get(client):
    """Test case for app_service_environments_get

    Get the properties of an App Service Environment.
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

async def test_app_service_environments_get_diagnostics_item(client):
    """Test case for app_service_environments_get_diagnostics_item

    Get a diagnostics item for an App Service Environment.
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

async def test_app_service_environments_get_multi_role_pool(client):
    """Test case for app_service_environments_get_multi_role_pool

    Get properties of a multi-role pool.
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

async def test_app_service_environments_get_worker_pool(client):
    """Test case for app_service_environments_get_worker_pool

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

async def test_app_service_environments_list(client):
    """Test case for app_service_environments_list

    Get all App Service Environments for a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/hostingEnvironments'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_environments_list_app_service_plans(client):
    """Test case for app_service_environments_list_app_service_plans

    Get all App Service plans in an App Service Environment.
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

async def test_app_service_environments_list_by_resource_group(client):
    """Test case for app_service_environments_list_by_resource_group

    Get all App Service Environments in a resource group.
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

async def test_app_service_environments_list_capacities(client):
    """Test case for app_service_environments_list_capacities

    Get the used, available, and total worker capacity an App Service Environment.
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

async def test_app_service_environments_list_diagnostics(client):
    """Test case for app_service_environments_list_diagnostics

    Get diagnostic information for an App Service Environment.
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

async def test_app_service_environments_list_metric_definitions(client):
    """Test case for app_service_environments_list_metric_definitions

    Get global metric definitions of an App Service Environment.
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

async def test_app_service_environments_list_metrics(client):
    """Test case for app_service_environments_list_metrics

    Get global metrics of an App Service Environment.
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

async def test_app_service_environments_list_multi_role_metric_definitions(client):
    """Test case for app_service_environments_list_multi_role_metric_definitions

    Get metric definitions for a multi-role pool of an App Service Environment.
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

async def test_app_service_environments_list_multi_role_metrics(client):
    """Test case for app_service_environments_list_multi_role_metrics

    Get metrics for a multi-role pool of an App Service Environment.
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

async def test_app_service_environments_list_multi_role_pool_instance_metric_definitions(client):
    """Test case for app_service_environments_list_multi_role_pool_instance_metric_definitions

    Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.
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

async def test_app_service_environments_list_multi_role_pool_instance_metrics(client):
    """Test case for app_service_environments_list_multi_role_pool_instance_metrics

    Get metrics for a specific instance of a multi-role pool of an App Service Environment.
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

async def test_app_service_environments_list_multi_role_pool_skus(client):
    """Test case for app_service_environments_list_multi_role_pool_skus

    Get available SKUs for scaling a multi-role pool.
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

async def test_app_service_environments_list_multi_role_pools(client):
    """Test case for app_service_environments_list_multi_role_pools

    Get all multi-role pools.
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

async def test_app_service_environments_list_multi_role_usages(client):
    """Test case for app_service_environments_list_multi_role_usages

    Get usage metrics for a multi-role pool of an App Service Environment.
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

async def test_app_service_environments_list_operations(client):
    """Test case for app_service_environments_list_operations

    List all currently running operations on the App Service Environment.
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

async def test_app_service_environments_list_usages(client):
    """Test case for app_service_environments_list_usages

    Get global usage metrics of an App Service Environment.
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

async def test_app_service_environments_list_vips(client):
    """Test case for app_service_environments_list_vips

    Get IP addresses assigned to an App Service Environment.
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

async def test_app_service_environments_list_web_apps(client):
    """Test case for app_service_environments_list_web_apps

    Get all apps in an App Service Environment.
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

async def test_app_service_environments_list_web_worker_metric_definitions(client):
    """Test case for app_service_environments_list_web_worker_metric_definitions

    Get metric definitions for a worker pool of an App Service Environment.
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

async def test_app_service_environments_list_web_worker_metrics(client):
    """Test case for app_service_environments_list_web_worker_metrics

    Get metrics for a worker pool of a AppServiceEnvironment (App Service Environment).
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

async def test_app_service_environments_list_web_worker_usages(client):
    """Test case for app_service_environments_list_web_worker_usages

    Get usage metrics for a worker pool of an App Service Environment.
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

async def test_app_service_environments_list_worker_pool_instance_metric_definitions(client):
    """Test case for app_service_environments_list_worker_pool_instance_metric_definitions

    Get metric definitions for a specific instance of a worker pool of an App Service Environment.
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

async def test_app_service_environments_list_worker_pool_instance_metrics(client):
    """Test case for app_service_environments_list_worker_pool_instance_metrics

    Get metrics for a specific instance of a worker pool of an App Service Environment.
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

async def test_app_service_environments_list_worker_pool_skus(client):
    """Test case for app_service_environments_list_worker_pool_skus

    Get available SKUs for scaling a worker pool.
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

async def test_app_service_environments_list_worker_pools(client):
    """Test case for app_service_environments_list_worker_pools

    Get all worker pools of an App Service Environment.
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

async def test_app_service_environments_reboot(client):
    """Test case for app_service_environments_reboot

    Reboot all machines in an App Service Environment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
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

async def test_app_service_environments_resume(client):
    """Test case for app_service_environments_resume

    Resume an App Service Environment.
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

async def test_app_service_environments_suspend(client):
    """Test case for app_service_environments_suspend

    Suspend an App Service Environment.
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


pytestmark = pytest.mark.asyncio

async def test_app_service_environments_update(client):
    """Test case for app_service_environments_update

    Create or update an App Service Environment.
    """
    hosting_environment_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=hosting_environment_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_environments_update_multi_role_pool(client):
    """Test case for app_service_environments_update_multi_role_pool

    Create or update a multi-role pool.
    """
    multi_role_pool_envelope = {"sku":"{}","properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=multi_role_pool_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_environments_update_worker_pool(client):
    """Test case for app_service_environments_update_worker_pool

    Create or update a worker pool.
    """
    worker_pool_envelope = {"sku":"{}","properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{worker_pool_name}'.format(resource_group_name='resource_group_name_example', name='name_example', worker_pool_name='worker_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=worker_pool_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

