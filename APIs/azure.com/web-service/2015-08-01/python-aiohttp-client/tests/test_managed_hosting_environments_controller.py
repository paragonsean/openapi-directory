# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_response import AddressResponse
from openapi_server.models.hosting_environment import HostingEnvironment
from openapi_server.models.hosting_environment_collection import HostingEnvironmentCollection
from openapi_server.models.managed_hosting_environment import ManagedHostingEnvironment
from openapi_server.models.server_farm_collection import ServerFarmCollection
from openapi_server.models.site_collection import SiteCollection


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_managed_hosting_environments_create_or_update_managed_hosting_environment(client):
    """Test case for managed_hosting_environments_create_or_update_managed_hosting_environment

    Create or update a managed hosting environment.
    """
    managed_hosting_environment_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/managedHostingEnvironments/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=managed_hosting_environment_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_hosting_environments_delete_managed_hosting_environment(client):
    """Test case for managed_hosting_environments_delete_managed_hosting_environment

    Delete a managed hosting environment.
    """
    params = [('forceDelete', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/managedHostingEnvironments/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_hosting_environments_get_managed_hosting_environment(client):
    """Test case for managed_hosting_environments_get_managed_hosting_environment

    Get properties of a managed hosting environment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/managedHostingEnvironments/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_hosting_environments_get_managed_hosting_environment_operation(client):
    """Test case for managed_hosting_environments_get_managed_hosting_environment_operation

    Get status of an operation on a managed hosting environment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/managedHostingEnvironments/{name}/operations/{operation_id}'.format(resource_group_name='resource_group_name_example', name='name_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_hosting_environments_get_managed_hosting_environment_server_farms(client):
    """Test case for managed_hosting_environments_get_managed_hosting_environment_server_farms

    Get all serverfarms (App Service Plans) on the managed hosting environment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/managedHostingEnvironments/{name}/serverfarms'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_hosting_environments_get_managed_hosting_environment_sites(client):
    """Test case for managed_hosting_environments_get_managed_hosting_environment_sites

    Get all sites on the managed hosting environment.
    """
    params = [('propertiesToInclude', 'properties_to_include_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/managedHostingEnvironments/{name}/sites'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_hosting_environments_get_managed_hosting_environment_vips(client):
    """Test case for managed_hosting_environments_get_managed_hosting_environment_vips

    Get list of ip addresses assigned to a managed hosting environment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/managedHostingEnvironments/{name}/capacities/virtualip'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_hosting_environments_get_managed_hosting_environment_web_hosting_plans(client):
    """Test case for managed_hosting_environments_get_managed_hosting_environment_web_hosting_plans

    Get all serverfarms (App Service Plans) on the managed hosting environment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/managedHostingEnvironments/{name}/webhostingplans'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_hosting_environments_get_managed_hosting_environments(client):
    """Test case for managed_hosting_environments_get_managed_hosting_environments

    Get all managed hosting environments in a resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/managedHostingEnvironments'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

