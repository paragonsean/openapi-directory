# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.avatar import Avatar
from openapi_server.models.avatars import Avatars
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.system_avatars import SystemAvatars


pytestmark = pytest.mark.asyncio

async def test_delete_avatar(client):
    """Test case for delete_avatar

    Delete avatar
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/universal_avatar/type/{type}/owner/{owning_object_id}/avatar/{id}'.format(type='type_example', owning_object_id='owning_object_id_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_system_avatars(client):
    """Test case for get_all_system_avatars

    Get system avatars by type
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/avatar/{type}/system'.format(type='project'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_avatar_image_by_id(client):
    """Test case for get_avatar_image_by_id

    Get avatar image by ID
    """
    params = [('size', 'size_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/universal_avatar/view/type/{type}/avatar/{id}'.format(type='type_example', id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_avatar_image_by_owner(client):
    """Test case for get_avatar_image_by_owner

    Get avatar image by owner
    """
    params = [('size', 'size_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/universal_avatar/view/type/{type}/owner/{entity_id}'.format(type='type_example', entity_id='entity_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_avatar_image_by_type(client):
    """Test case for get_avatar_image_by_type

    Get avatar image by type
    """
    params = [('size', 'size_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/universal_avatar/view/type/{type}'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_avatars(client):
    """Test case for get_avatars

    Get avatars
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/universal_avatar/type/{type}/owner/{entity_id}'.format(type='type_example', entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_store_avatar(client):
    """Test case for store_avatar

    Load avatar
    """
    body = None
    params = [('x', 0),
                    ('y', 0),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/universal_avatar/type/{type}/owner/{entity_id}'.format(type='type_example', entity_id='entity_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

