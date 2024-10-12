# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.tag_details import TagDetails
from openapi_server.models.tag_value import TagValue
from openapi_server.models.tags_list_result import TagsListResult
from openapi_server.models.tags_patch_resource import TagsPatchResource
from openapi_server.models.tags_resource import TagsResource


pytestmark = pytest.mark.asyncio

async def test_tags_create_or_update(client):
    """Test case for tags_create_or_update

    Creates a predefined tag name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/tagNames/{tag_name}'.format(tag_name='tag_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_create_or_update_at_scope(client):
    """Test case for tags_create_or_update_at_scope

    Creates or updates the entire set of tags on a resource or subscription.
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"tags":{"key":"tags"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Resources/tags/default'.format(scope='scope_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_create_or_update_value(client):
    """Test case for tags_create_or_update_value

    Creates a predefined value for a predefined tag name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/tagNames/{tag_name}/tagValues/{tag_value}'.format(tag_name='tag_name_example', tag_value='tag_value_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_delete(client):
    """Test case for tags_delete

    Deletes a predefined tag name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/tagNames/{tag_name}'.format(tag_name='tag_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_delete_at_scope(client):
    """Test case for tags_delete_at_scope

    Deletes the entire set of tags on a resource or subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.Resources/tags/default'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_delete_value(client):
    """Test case for tags_delete_value

    Deletes a predefined tag value for a predefined tag name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/tagNames/{tag_name}/tagValues/{tag_value}'.format(tag_name='tag_name_example', tag_value='tag_value_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_get_at_scope(client):
    """Test case for tags_get_at_scope

    Gets the entire set of tags on a resource or subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Resources/tags/default'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_list(client):
    """Test case for tags_list

    Gets a summary of tag usage under the subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/tagNames'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_update_at_scope(client):
    """Test case for tags_update_at_scope

    Selectively updates the set of tags on a resource or subscription.
    """
    parameters = {"operation":"Replace","properties":{"tags":{"key":"tags"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{scope}/providers/Microsoft.Resources/tags/default'.format(scope='scope_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

