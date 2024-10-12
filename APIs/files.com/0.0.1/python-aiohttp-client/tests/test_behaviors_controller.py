# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.behavior_entity import BehaviorEntity
from openapi_server.models.status_entity import StatusEntity


pytestmark = pytest.mark.asyncio

async def test_behavior_list_for_path(client):
    """Test case for behavior_list_for_path

    List Behaviors by path
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_prefix', None),
                    ('recursive', 'recursive_example'),
                    ('behavior', 'behavior_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/behaviors/folders/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_behaviors_id(client):
    """Test case for delete_behaviors_id

    Delete Behavior
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/behaviors/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_behaviors(client):
    """Test case for get_behaviors

    List Behaviors
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('behavior', 'behavior_example'),
                    ('filter', None),
                    ('filter_prefix', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/behaviors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_behaviors_id(client):
    """Test case for get_behaviors_id

    Show Behavior
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/behaviors/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_behaviors_id(client):
    """Test case for patch_behaviors_id

    Update Behavior
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('attachment_delete', True)
    data.add_field('attachment_file', '/path/to/file')
    data.add_field('behavior', 'behavior_example')
    data.add_field('description', 'description_example')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    data.add_field('value', 'value_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/behaviors/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_behaviors(client):
    """Test case for post_behaviors

    Create Behavior
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('attachment_file', '/path/to/file')
    data.add_field('behavior', 'behavior_example')
    data.add_field('description', 'description_example')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    data.add_field('value', 'value_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/behaviors',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_behaviors_webhook_test(client):
    """Test case for post_behaviors_webhook_test

    Test webhook.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('action', 'action_example')
    data.add_field('body', None)
    data.add_field('encoding', 'encoding_example')
    data.add_field('headers', None)
    data.add_field('method', 'method_example')
    data.add_field('url', 'url_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/behaviors/webhook/test',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

