# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_health_metadata import ResourceHealthMetadata
from openapi_server.models.resource_health_metadata_collection import ResourceHealthMetadataCollection
from openapi_server.models.resource_health_metadata_list_default_response import ResourceHealthMetadataListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_resource_health_metadata_get_by_site(client):
    """Test case for resource_health_metadata_get_by_site

    Gets the category of ResourceHealthMetadata to use for the given site
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/resourceHealthMetadata/default'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_health_metadata_get_by_site_slot(client):
    """Test case for resource_health_metadata_get_by_site_slot

    Gets the category of ResourceHealthMetadata to use for the given site
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resourceHealthMetadata/default'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_health_metadata_list(client):
    """Test case for resource_health_metadata_list

    List all ResourceHealthMetadata for all sites in the subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/resourceHealthMetadata'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_health_metadata_list_by_resource_group(client):
    """Test case for resource_health_metadata_list_by_resource_group

    List all ResourceHealthMetadata for all sites in the resource group in the subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/resourceHealthMetadata'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_health_metadata_list_by_site(client):
    """Test case for resource_health_metadata_list_by_site

    Gets the category of ResourceHealthMetadata to use for the given site as a collection
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/resourceHealthMetadata'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_health_metadata_list_by_site_slot(client):
    """Test case for resource_health_metadata_list_by_site_slot

    Gets the category of ResourceHealthMetadata to use for the given site as a collection
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resourceHealthMetadata'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

