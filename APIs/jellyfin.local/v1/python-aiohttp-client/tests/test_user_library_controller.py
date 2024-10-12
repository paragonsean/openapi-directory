# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.user_item_data_dto import UserItemDataDto


pytestmark = pytest.mark.asyncio

async def test_delete_user_item_rating(client):
    """Test case for delete_user_item_rating

    Deletes a user's saved personal rating for an item.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Users/{user_id}/Items/{item_id}/Rating'.format(user_id='user_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_intros(client):
    """Test case for get_intros

    Gets intros to play before the main media item plays.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Items/{item_id}/Intros'.format(user_id='user_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item(client):
    """Test case for get_item

    Gets an item from a user's library.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Items/{item_id}'.format(user_id='user_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_media(client):
    """Test case for get_latest_media

    Gets latest media.
    """
    params = [('parentId', 'parent_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('includeItemTypes', ['include_item_types_example']),
                    ('isPlayed', True),
                    ('enableImages', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('enableUserData', True),
                    ('limit', 20),
                    ('groupItems', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Items/Latest'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_local_trailers(client):
    """Test case for get_local_trailers

    Gets local trailers for an item.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Items/{item_id}/LocalTrailers'.format(user_id='user_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_root_folder(client):
    """Test case for get_root_folder

    Gets the root folder from a user's library.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Items/Root'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_special_features(client):
    """Test case for get_special_features

    Gets special features for an item.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Items/{item_id}/SpecialFeatures'.format(user_id='user_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_favorite_item(client):
    """Test case for mark_favorite_item

    Marks an item as a favorite.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}/FavoriteItems/{item_id}'.format(user_id='user_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unmark_favorite_item(client):
    """Test case for unmark_favorite_item

    Unmarks item as a favorite.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Users/{user_id}/FavoriteItems/{item_id}'.format(user_id='user_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user_item_rating(client):
    """Test case for update_user_item_rating

    Updates a user's rating for an item.
    """
    params = [('likes', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}/Items/{item_id}/Rating'.format(user_id='user_id_example', item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

