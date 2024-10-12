# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_insights_component_favorite import ApplicationInsightsComponentFavorite


pytestmark = pytest.mark.asyncio

async def test_favorites_add(client):
    """Test case for favorites_add

    
    """
    favorite_properties = {"FavoriteId":"FavoriteId","TimeModified":"TimeModified","Category":"Category","Version":"Version","Config":"Config","UserId":"UserId","SourceType":"SourceType","FavoriteType":"shared","IsGeneratedFromTemplate":True,"Tags":["Tags","Tags"],"Name":"Name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/favorites/{favorite_id}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example', favorite_id='favorite_id_example'),
        headers=headers,
        json=favorite_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_favorites_delete(client):
    """Test case for favorites_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/favorites/{favorite_id}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example', favorite_id='favorite_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_favorites_get(client):
    """Test case for favorites_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/favorites/{favorite_id}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example', favorite_id='favorite_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_favorites_list(client):
    """Test case for favorites_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('favoriteType', shared),
                    ('sourceType', 'source_type_example'),
                    ('canFetchContent', True),
                    ('tags', ['tags_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/favorites'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_favorites_update(client):
    """Test case for favorites_update

    
    """
    favorite_properties = {"FavoriteId":"FavoriteId","TimeModified":"TimeModified","Category":"Category","Version":"Version","Config":"Config","UserId":"UserId","SourceType":"SourceType","FavoriteType":"shared","IsGeneratedFromTemplate":True,"Tags":["Tags","Tags"],"Name":"Name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/favorites/{favorite_id}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example', favorite_id='favorite_id_example'),
        headers=headers,
        json=favorite_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

